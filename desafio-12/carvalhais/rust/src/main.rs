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
