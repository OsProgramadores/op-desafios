#![allow(unused_variables)]
#![allow(unused_imports)]
#![feature(platform_intrinsics)]
#![feature(repr_simd)]

mod fields;
mod parser;
mod simd;
mod stats;
mod utils;
use fields::{Areas, Empresa, Funcionario, Text};
use parser::{AreasParser, FuncsParser};
use simd::u8x32;
use stats::Stats;
use utils::Aoc;

use crossbeam_channel::{self as channel, select, Receiver, Sender};
use scoped_threadpool::Pool;
use std::fs::File;
use std::sync::Arc;

fn get_thread_range(size: usize, nth: usize, max: usize) -> (usize, usize) {
    let slice = size / max;
    let min = slice * nth;
    let max = min + slice;
    (min, max)
}

#[derive(Debug)]
struct GetFuncsThreadSliceError;
fn get_funcs_thread_slice(funcs: &[u8], size: usize) -> Result<&[u8], GetFuncsThreadSliceError> {
    // get beginning
    let begin = funcs[..size].iter().position(|&it| it == b'{');
    if begin.is_none() {
        return Ok(&[]);
    }
    let begin = begin.unwrap();

    // get ending
    let end = if funcs.len() == size {
        0
    } else {
        funcs[size..]
            .iter()
            .position(|&it| it == b'{')
            .ok_or(GetFuncsThreadSliceError)?
    };

    let quotes = funcs[..size + end]
        .iter()
        .rev()
        .position(|&it| it == b'"')
        .ok_or(GetFuncsThreadSliceError)?;

    Ok(&funcs[begin..size + end - quotes])
}

pub fn get_stats(data: &[u8], num_threads: u32) -> Option<Empresa<'_>> {
    let mut pool = Pool::new(num_threads);
    let num_threads = num_threads as usize;
    let (chan_stats_s, chan_stats_r) = channel::bounded(num_threads);
    let (chan_close_s, chan_close_r) = channel::bounded(num_threads);

    // Phase 1: Parsing - Areas
    let (funcs, areas) = parse_areas(data);

    pool.scoped(|scope| {
        // Phase 2: Parsing - Funcionarios

        // Phase 2.1: First Threads
        for idx in 0..num_threads - 1 {
            let chan_stats = chan_stats_s.clone();
            let chan_close = chan_close_s.clone();

            scope.execute(move || {
                let (min, max) = get_thread_range(funcs.len(), idx, num_threads);

                let slice = if idx == 0 {
                    let begin = funcs
                        .iter()
                        .position(|&it| it == b'{')
                        .expect("malformed input");
                    get_funcs_thread_slice(&funcs[begin + 1..], max - min - begin - 1)
                } else {
                    get_funcs_thread_slice(&funcs[min..], max - min)
                };

                let slice = slice.expect("malformed input");
                parse_funcs(slice, chan_stats, chan_close, false);
            });
        }

        // Phase 2.2: Last Thread
        {
            let chan_close = chan_close_s.clone();
            let chan_stats = chan_stats_s.clone();

            scope.execute(move || {
                let (min, _) = get_thread_range(funcs.len(), num_threads - 1, num_threads);
                let size = funcs[min..].len();
                let slice = get_funcs_thread_slice(&funcs[min..], size).expect("malformed input");
                parse_funcs(slice, chan_stats, chan_close, true);
            });
        }

        // Phase 3: Stats Merge
        for _ in 1..num_threads {
            let chan_stats_s = chan_stats_s.clone();
            let chan_stats_r = chan_stats_r.clone();
            let chan_close_s = chan_close_s.clone();
            let chan_close_r = chan_close_r.clone();

            scope.execute(move || {
                merge_stats(chan_stats_s, chan_stats_r, chan_close_s, chan_close_r)
            });
        }
        drop(chan_stats_s);
        drop(chan_close_s);
        drop(chan_close_r);
    });

    // Phase 4: Stats Merge (final)
    let mut stats = chan_stats_r.recv().ok()?;
    chan_stats_r.iter().for_each(|it| stats.merge(it));
    Some(Empresa::new(stats, areas))
}

pub fn parse_areas(text: &[u8]) -> (&'_ [u8], Areas<'_>) {
    let mut parser = AreasParser::new(text);
    let mut areas = Areas::default();

    let rbracket;
    loop {
        let (nome, pos) = parser.get_string();

        // TODO: find a better way to do it
        if nome == "areas" {
            rbracket = parser.osp_rbracket(pos);
            assert!(rbracket != 0, "malformed input");
            break;
        }

        parser.skip_string();
        let codigo = parser.osp_get_area();

        areas.insert(codigo, nome);
        parser.skip_string();
    }

    (&text[..rbracket - 1], areas)
}

fn parse_funcs<'a>(
    text: &'a [u8],
    chan_stats: Sender<Stats<'a>>,
    chan_close: Sender<()>,
    is_last: bool,
) {
    fn parse_func<'a, F, R>(parser: &mut FuncsParser<'a>, mut f: F) -> R
    where
        F: FnMut(Funcionario<'a>) -> R,
    {
        // skip "id" key
        parser.skip_string();
        // skip "nome" key
        parser.skip_string();
        // get "nome" value
        let nome = parser.get_string().0;
        // skip "sobrenome" key
        parser.skip_string();
        // get "sobrenome" value
        let sobrenome = parser.get_string().0;
        // skip "salario" key
        let idx = parser.skip_string().1;
        // get "salario" value
        let salario = parser.osp_get_salary(idx + 2);
        // skip "area" key
        parser.skip_string();

        // get "area" value
        let area = parser.osp_get_area();

        f(Funcionario::new(nome, sobrenome, salario, area))
    }

    let mut parser = FuncsParser::new(text);

    if parser.is_done() {
        chan_close.send(()).expect("SenderFail");
        return;
    }

    let mut stats = parse_func(&mut parser, Stats::new);

    while !parser.is_done() {
        parse_func(&mut parser, |func| stats.update(Aoc::new(func)));
    }

    if is_last {
        chan_close.send(()).expect("SenderFail");
    }

    chan_stats.send(stats).expect("SenderFail");
}

fn merge_stats<'a>(
    chan_stats_s: Sender<Stats<'a>>,
    chan_stats_r: Receiver<Stats<'a>>,
    chan_close_s: Sender<()>,
    chan_close_r: Receiver<()>,
) {
    let mut stats = chan_stats_r.recv().expect("RecvError");

    select! {
        recv(chan_close_r) -> _ => {},
        recv(chan_stats_r) -> stats2 => {
            stats.merge(stats2.unwrap());
        },
    };

    chan_stats_s.send(stats).expect("SenderFail");
}
