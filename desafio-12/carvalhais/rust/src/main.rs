// A vanilla Rust solution for challenge #12 from OsProgramadores website
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

// use the num_bigint crate for the moment being, since the big integer helper
// methods are still experimental in the rust API at the time of this writing
// (2022-02-03)
//
// TODO: implement from scratch a nice popcount algoritm (possible candidates:
// sideways sum, SWAR, etc), and write a nice article on the README.md file
// explaining how it works
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;
use num_bigint::BigUint;


fn main() {
    let filename = std::env::args().nth(1).expect("no filename given");
    let filename = PathBuf::from(filename);
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line.unwrap();
        let line = line.trim();
        let number = BigUint::parse_bytes(line.as_bytes(), 10).unwrap();
        let popcount = number.count_ones();
        if popcount == 1 {
            let exponent = number.trailing_zeros().unwrap();
            println!("{} true {}", number, exponent);
        }
        else {
            println!("{} false", number);
        }
    }
}
