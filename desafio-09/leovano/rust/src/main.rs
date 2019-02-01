use num_bigint::BigUint;
use num_integer::Integer;
use num_traits::cast::ToPrimitive;

mod conv_error;
use self::conv_error::ConvError;

use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

macro_rules! ensure {
    ($pred:expr, $error:expr) => {
        if !$pred {
            return $error;
        }
    };
}

const ENC_TABLE: [char; 62] = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
];

fn parse(orig: u8, input: &str) -> Result<BigUint, ConvError> {
    ensure!(orig >= 2 && orig <= 62, Err(ConvError::InvalidRadix));

    let mut num = BigUint::default();

    for ch in input.chars() {
        let dec = ENC_TABLE
            .iter()
            .position(|it| ch == *it)
            .ok_or(ConvError::InvalidCharacter)?;
        ensure!(
            dec < orig as usize,
            Err(ConvError::InvalidCharacterForRadix)
        );

        num *= orig;
        num += BigUint::from(dec);
    }

    Ok(num)
}

fn convert(dest: u8, mut num: BigUint) -> Result<Vec<u8>, ConvError> {
    ensure!(dest >= 2 && dest <= 62, Err(ConvError::InvalidRadix));

    let zero = BigUint::default();
    let dest = BigUint::from(dest);
    let mut res = vec![];

    while num > zero {
        let (d, m) = num.div_rem(&dest);
        num = d;
        res.push(m.to_u8().unwrap());
    }

    if res.is_empty() {
        res.push(0);
    }

    Ok(res)
}

fn to_str_radix(line: &str, max: &BigUint) -> Result<Vec<u8>, ConvError> {
    let line: Vec<&str> = line.split(' ').filter(|it| !it.is_empty()).collect();
    ensure!(line.len() == 3, Err(ConvError::InvalidInput));

    let orig: u8 = line[0].parse()?;
    let dest: u8 = line[1].parse()?;

    ensure!(dest >= 2 && dest <= 62, Err(ConvError::InvalidRadix));

    // Parse
    let num = parse(orig, line[2])?;
    ensure!(&num <= max, Err(ConvError::TooBigNumber));

    // Convert
    let res = convert(dest, num)?;

    Ok(res)
}

fn main() {
    let file = env::args().nth(1).expect("Arg1");
    let file = File::open(file).expect("FileFail");
    let file = BufReader::new(file);

    let max = parse(62, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz").unwrap();

    for line in file.lines() {
        let line = line.expect("ReadFail");

        if let Ok(num) = to_str_radix(&line, &max) {
            num.into_iter()
                .rev()
                .for_each(|ch| print!("{}", ENC_TABLE[ch as usize]));
            println!();
        } else {
            println!("???");
        }
    }
}

