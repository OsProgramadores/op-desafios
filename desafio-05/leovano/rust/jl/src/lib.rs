#![feature(const_fn)]
#![feature(platform_intrinsics)]
#![feature(repr_simd)]
#![feature(tool_lints)]

#[macro_use]
extern crate cfg_if;
extern crate crossbeam_channel;
extern crate scoped_threadpool;
extern crate jemallocator;

mod fields;
mod simd;
mod stats;
mod utils;
use self::{
    fields::{Areas, Empresa, Funcionario},
    simd::u8x32,
    stats::Stats,
    utils::Parser,
};

use crossbeam_channel::unbounded as channel;
use crossbeam_channel::{Receiver, Sender};
use scoped_threadpool::Pool;
use std::io;

#[global_allocator]
static ALLOC: jemallocator::Jemalloc = jemallocator::Jemalloc;

pub fn get_stats<'a>(
    json: &'a [u8],
    num_cpus: u32,
) -> Result<Empresa<'a>, io::Error> {
    let mut pool = Pool::new(num_cpus);
    let mut stats = Stats::default();
    let (chan_fns_s, chan_fns_r): (
        Sender<Funcionario<'a>>,
        Receiver<Funcionario<'a>>,
    ) = channel();
    let (chan_sts_s, chan_sts_r): (
        Sender<Stats<'a>>, //
        Receiver<Stats<'a>>,
    ) = channel();

    let mut areas = Areas::default();
    pool.scoped(|scope| {
        // Phase 1: Parsing
        scope.execute(|| areas = parse(json, chan_fns_s));

        // Phase 2: StatsGen
        for _n in 0..num_cpus {
            let chan_fns_r = chan_fns_r.clone();
            let chan_sts_s = chan_sts_s.clone();
            scope.execute(move || {
                let stats = match chan_fns_r.recv() {
                    Some(rs) => rs,
                    None => return,
                };
                let mut stats = Stats::from_single(stats);
                for func in chan_fns_r {
                    stats.update(func);
                }
                chan_sts_s.send(stats);
            });
        }
        drop(chan_sts_s);

        // Phase 3: StatsMerge
        scope.execute(|| {
            stats = chan_sts_r.recv().unwrap_or_default();
            for sts in chan_sts_r {
                stats.merge(sts);
            }
        });
    });

    Ok(Empresa::new(stats, areas))
}

fn parse<'a>(file: &'a [u8], chan: Sender<Funcionario<'a>>) -> Areas<'a> {
    let mut parser = Parser::new(file);

    // skip "funcionarios" key
    parser.skip_string();

    while parser.osp_rbracket() == 64 {
        // skip "id" key
        parser.skip_string();
        // skip "nome" key
        parser.skip_string();
        // get "nome" value
        let nome = parser.get_string();
        // skip "sobrenome" key
        parser.skip_string();
        // get "sobrenome" value
        let sobrenome = parser.get_string();
        // skip "salario" key
        let idx = parser.skip_string();
        // get "salario" value
        let salario = u64::from(parser.osp_get_salary(idx + 2));
        // skip "area" key
        parser.skip_string();
        // get "area" value
        let area = parser.osp_get_area();

        chan.send(Funcionario::new(nome, sobrenome, salario, area));
    }

    // skip "areas" key
    parser.skip_string();

    let mut areas = Areas::default();

    // skip "codigo" key
    while !parser.is_done() && parser.skip_string() != 64 {
        // get "codigo" value
        let codigo = parser.osp_get_area();
        // skip "nome" key
        parser.skip_string();
        // get "nome" value
        let nome = parser.get_string();

        areas.insert(codigo, nome);
    }

    drop(chan);
    areas
}
