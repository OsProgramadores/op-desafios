use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn gcd(a: i64, b: i64) -> i64 {
    if a == 0 {
        b
    } else {
        gcd(b % a, a)
    }
}

fn simplify(num: i64, den: i64) -> Option<(i64, i64, i64)> {
    if den == 0 {
        return None;
    }

    let (int, num) = (num / den, num % den);
    let gcd = gcd(num, den);
    let (num, den) = (num / gcd, den / gcd);

    Some((int, num, den))
}

#[test]
fn test_simplify() {
    assert_eq!(simplify(14, 3), Some((4, 2, 3)));
    assert_eq!(simplify(3, 8), Some((0, 3, 8)));
    assert_eq!(simplify(4, 8), Some((0, 1, 2)));
    assert_eq!(simplify(4, 3), Some((1, 1, 3)));
    assert_eq!(simplify(5, 1), Some((5, 0, 1)));
    assert_eq!(simplify(10, 0), None)
}

fn main() {
    let file = env::args().nth(1).expect("Arg1");
    let file = File::open(file).expect("FileFail");
    let file = BufReader::new(file);

    for line in file.lines() {
        let frac = line.expect("LineFail");
        let mut frac = frac.split('/');

        let num = frac
            .next()
            .and_then(|it| it.parse::<i64>().ok())
            .expect("ParseFail");
        let den = frac
            .next()
            .map_or(Ok(1), |it| it.parse::<i64>())
            .expect("ParseFail");

        if let Some((int, num, den)) = simplify(num, den) {
            if int != 0 {
                print!("{} ", int);
            }
            if num != 0 {
                print!("{}/{}", num, den);
            }
            println!();
        } else {
            println!("ERR");
        }
    }
}
