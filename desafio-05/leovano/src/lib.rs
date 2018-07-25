#[macro_use]
extern crate serde_derive;
extern crate fnv;
extern crate indexmap;
extern crate serde;
extern crate serde_json;

mod error;
mod fields;
mod misc;
mod stats;
pub use error::Error;
pub use fields::Empresa;
pub use stats::Stats;

use std::fs::File;
use std::io::Read;

pub fn parse<'a>(out: &'a mut String, json: &'a str) -> Result<Empresa<'a>, Error> {
    File::open(json)?.read_to_string(out)?;
    Ok(serde_json::from_str(out)?)
}

pub fn get_stats<'a>(j: &'a Empresa<'a>) -> Stats<'a> {
    let fst = &j.funcionarios[0];
    let snd = &j.funcionarios[1];

    let mut stats = Stats::from_duo(fst, snd);

    for f in &j.funcionarios[2..] {
        stats.update(f);
    }

    stats
}
