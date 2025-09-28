fn is_prime(num: u16) -> bool {
    let limit = f64::sqrt(num as f64) as u16 + 1;
    for j in 2..limit {
        if num % j == 0 {
            return false;
        }
    }
    return true;
}

fn main() {
    for i in 2..10001 {
        if is_prime(i) {
            println!("{}", i);
        }
    }
}
