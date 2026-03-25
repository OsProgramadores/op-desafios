// Autor: Leo Silva Souza

use std::io::{stdin, stdout, Write};

// Rust doesn't have a built-in for that
// So, I need to implement it myself.
fn prompt(msg: &str) -> u64 {
    print!("{}", msg);
    stdout().flush().unwrap();

    let buf = &mut String::new();
    stdin().read_line(buf).unwrap();
    buf.pop();
    buf.parse().expect("Número inválido!")
}

mod palindrome {
    pub fn test(n: u64) -> bool {
        let m = (0..).map(|i| 10u64.pow(i)).find(|i| n / i < 10).unwrap();
        rec_test(m, n)
    }

    fn rec_test(m: u64, n: u64) -> bool {
        m == 0 || (n / m == n % 10 && rec_test(m / 100, n % m / 10))
    }
}

fn main() {
    let fst = prompt("Primeiro: ");
    let snd = prompt("Último: ");
    (fst..=snd)
        .filter(|n| palindrome::test(*n))
        .for_each(|n| println!("{}", n));
}
