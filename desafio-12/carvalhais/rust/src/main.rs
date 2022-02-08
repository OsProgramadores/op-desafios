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
extern crate clap;
extern crate num_bigint;

use clap::Parser;
use num_bigint::BigUint;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

#[derive(Parser)]
#[clap(about, version, author)]
// Holds the command line arguments given to the application
struct CliOptions {
    /// outputs a nicely formatted table with big numbers shortened
    #[clap(long)]
    tabular: bool,

    /// files to load the numbers from, one per line
    #[clap(parse(from_os_str))]
    filename: PathBuf,
}

fn main() {
    let opts = CliOptions::parse();
    let file = match File::open(&opts.filename) {
        Ok(f) => f,
        Err(e) => {
            println!("{}: {}", e, opts.filename.to_string_lossy());
            return;
        }
    };
    let reader = BufReader::new(file);

    if opts.tabular {
        println!(
            " {:^4} | {:^20} | {:^6} | {:^6} | {:^6} ",
            "ID", "Number", "Digits", "Power", "Exp"
        );
        println!("{:-^6}|{:-^22}|{:-^8}|{:-^8}|{:-^8}", "", "", "", "", "");
    }

    for (index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let line = line.trim();
        let number = BigUint::parse_bytes(line.as_bytes(), 10).unwrap();
        let is_power = number.count_ones() == 1;
        let exponent = match is_power {
            true => Some(number.trailing_zeros().unwrap()),
            false => None,
        };
        if opts.tabular {
            let mut number = format!("{}", number);
            let num_digits = number.len();
            if num_digits > 20 {
                number = format!("{}...{}", &number[0..14], &number[num_digits - 3..]);
            }
            if is_power {
                println!(
                    " {:^4} | {:>20} | {:^6} | {:^6} | {:^6} ",
                    index,
                    number,
                    num_digits,
                    is_power,
                    exponent.unwrap()
                );
                continue;
            }
            println!(
                " {:^4} | {:>20} | {:^6} | {:^6} | {:^6} ",
                index, number, num_digits, is_power, "--"
            );
        } else {
            if is_power {
                println!("{} {} {}", number, is_power, exponent.unwrap());
                continue;
            }
            println!("{} {}", number, is_power);
        }
    }
}
