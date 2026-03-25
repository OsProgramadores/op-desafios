// Autor: Leo Silva Souza
// Example usage: `./main < sample_02.txt`

use std::io::{stdin, Read};

const NAMES: [&'static str; 6] = ["Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"];

fn main() {
    let mut count = [0u8; 7];

    let stdin = stdin();
    stdin
        .lock()
        .bytes()
        .filter_map(|b| (b.ok()? as char).to_digit(10))
        .for_each(|n| count[n as usize] += 1);

    for idx in 1..7 {
        println!("{}:\t{}", NAMES[idx - 1], count[idx]);
    }
}
