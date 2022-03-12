// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use clap::Parser;
use prelude::*;
use std::error;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

mod computer;
mod scanner;
mod shuntyard;
mod types;

pub mod prelude {
    pub use super::computer::compute;
    pub use super::scanner::scan;
    pub use super::shuntyard::shunt;
    pub use super::types::{Direction, ExprError, Procedure, Token};
}

#[derive(Parser)]
#[clap(about, version, author)]
// Holds the command line arguments given to the application, since it's not
// directly related to the shunting yeard algorithm functionality, it's not
// placed in the types module
pub struct Config {
    /// files to load expressions from, one per line
    #[clap(parse(from_os_str))]
    pub filename: PathBuf,
}

/// Attempts to compute an expression value from it's string representation
fn try_computation(expr: &str) -> Result<i64, ExprError> {
    let step = scan(expr)?;
    let step = shunt(step)?;
    compute(step)
}

/// Runs the main computing algorithm, handling any unrecoverable error to main
pub fn run(config: Config) -> Result<(), Box<dyn error::Error>> {
    let file = File::open(&config.filename)?;
    let reader = BufReader::new(file);
    let mut lines = reader.lines();

    while let Some(Ok(line)) = lines.next() {
        let result = try_computation(&line);
        let output = match result {
            Ok(value) => format!("{}", value),
            Err(ExprError::DivByZero) => "ERR DIVBYZERO".to_string(),
            Err(_) => "ERR SYNTAX".to_string(),
        };
        println!("{}", output);
    }
    Ok(())
}
