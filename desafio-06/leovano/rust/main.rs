use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

const WORDS_FILE: &str = "../words.txt";

type Word = Vec<char>;

pub struct Dict {
    words: Vec<Word>,
}

impl Dict {
    pub fn from_file(file: File) -> Self {
        let mut words = BufReader::new(file)
            .lines()
            .map(|it| it.expect("ReadFail").chars().collect())
            .collect::<Vec<Word>>();
        words.sort();
        Dict { words }
    }
}

mod anagram {
    use crate::{Dict, Word};

    fn string_diff(word: &mut Word, diff: &Word) -> Word {
        diff.iter()
            .filter_map(|ch| Some(word.remove(word.iter().position(|it| it == ch)?)))
            .collect()
    }

    pub fn for_each_do<F>(dict: &Dict, word: &str, f: F)
    where
        F: Fn(&Vec<&Word>),
    {
        let word = word
            .chars()
            .filter(|ch| ch.is_alphabetic())
            .map(|ch| ch.to_ascii_uppercase())
            .collect::<Word>();

        for_each_do_rec(dict.words.as_slice(), word, vec![], &f);
    }

    fn for_each_do_rec<'a, F>(
        words: &'a [Word],
        mut word: Word,
        mut acc: Vec<&'a Word>,
        f: &'a F,
    ) -> (Word, Vec<&'a Word>)
    where
        F: Fn(&Vec<&Word>),
    {
        if word.len() == 0 {
            f(&acc);
        } else {
            for (idx, dword) in words.iter().enumerate() {
                let diff = string_diff(&mut word, dword);
                if diff.len() == dword.len() {
                    acc.push(dword);
                    let res = for_each_do_rec(&words[idx + 1..], word, acc, f);
                    word = res.0;
                    acc = res.1;
                    acc.pop();
                }
                word.extend(diff);
            }
        }

        return (word, acc);
    }
}

fn main() {
    let word = env::args().nth(1).expect("Arg1");

    let file = File::open(WORDS_FILE).expect("FileFail");
    let dict = Dict::from_file(file);
    anagram::for_each_do(&dict, &word, |words| {
        for word in words {
            word.iter().for_each(|it| print!("{}", it));
            print!(" ");
        }
        println!();
    });
}
