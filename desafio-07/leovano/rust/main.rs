use std::fs::File;
use std::io::{BufReader, Read, Seek, SeekFrom};
use std::io::{StdoutLock, Write};
use std::{env, io};

const BUF_SIZE: usize = 128;

fn print_reversed(out: &mut StdoutLock<'_>, v: &mut Vec<u8>, buf: &[u8]) -> Result<(), io::Error> {
    let mut last = buf.len();
    let mut pos = buf.len();

    // 1st iteration: vec-aware
    while pos > 0 {
        if buf[pos - 1] == b'\n' {
            out.write(&buf[pos..])?;
            for &ch in v.iter().rev() {
                out.write(&[ch])?;
            }
            out.write(&[b'\n'])?;
            v.clear();
            last = pos;
            break;
        }

        pos -= 1;
    }

    // subsequent iterations
    while pos > 0 {
        if buf[pos - 1] == b'\n' {
            out.write(&buf[pos..last])?;
            last = pos;
        }

        pos -= 1;
    }

    Ok(v.extend((&buf[0..last - 1]).iter().rev()))
}

fn main() {
    let file = env::args().nth(1).expect("Arg1");
    let file = File::open(file).expect("FileFail");
    let file_len = file.metadata().expect("MetadataFail").len();
    let mut file = BufReader::new(file);

    let out = io::stdout();
    let mut out = out.lock();

    let buf = &mut [0u8; BUF_SIZE];
    let mut chars = Vec::with_capacity(BUF_SIZE);
    let mut pos = file_len / BUF_SIZE as u64 * BUF_SIZE as u64;

    // Print last bytes
    file.seek(SeekFrom::Start(pos)).unwrap();
    let read = file.read(buf).expect("ReadFail");
    print_reversed(&mut out, &mut chars, &buf[0..read - 1]).expect("ReadFail");

    // Print "middle" bytes
    loop {
        if pos < BUF_SIZE as u64 {
            break;
        }

        file.seek(SeekFrom::Start(pos - BUF_SIZE as u64)).unwrap();
        file.read(buf).expect("ReadFail");
        print_reversed(&mut out, &mut chars, buf).expect("ReadFail");

        pos -= BUF_SIZE as u64;
    }

    // Print first line
    for &ch in chars.iter().rev() {
        out.write(&[ch]).expect("WriteFail");
    }
    println!();
}
