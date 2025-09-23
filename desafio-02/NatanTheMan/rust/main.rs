use std::f32;

fn is_prime(num: i32) -> bool {
    let mut counter = 0;
    for j in 2..((num as f32).sqrt() as i32) + 1 {
        if num % j == 0 {
            counter += 1;
            if counter >= 1 {
                return false;
            }
        }
    }
    return true;
}

fn main() {
    for i in 2..101 {
        if is_prime(i) {
            println!("{}", i);
        }
    }
}
