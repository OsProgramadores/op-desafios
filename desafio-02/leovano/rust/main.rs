// Autor: Leo Silva Souza
// Requer Nightly.

#![feature(iterator_step_by)]

const MAX: usize = 10_000;

fn main() {
    let mut list = [false; MAX + 1];

    print!("2");
    for idx in (3..=MAX).step_by(2) {
        if !list[idx] {
            print!(", {}", idx);
            (idx..=MAX).step_by(idx).for_each(|i| list[i] = true);
        }
    }
    println!(".");
}
