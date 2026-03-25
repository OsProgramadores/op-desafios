// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use clap::Parser;
use solver;
use std::process;

fn main() {
    let config = solver::Config::parse();
    if let Err(e) = solver::run(config) {
        eprintln!("Application error: {}", e);
        process::exit(1);
    }
}
