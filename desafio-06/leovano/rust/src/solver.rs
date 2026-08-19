use std::{
    collections::HashMap,
    io::{self, BufRead},
};

use crate::freq::{Alphabet, LetterFreq, LetterFreqError};

pub struct CandidateGroup {
    pub frequency: LetterFreq,
    pub words: Vec<String>,
    pub word_len: usize,
}

pub struct Solver {
    groups: Vec<CandidateGroup>,
    target_freq: LetterFreq,
}

#[derive(thiserror::Error, Debug)]
pub enum SolverError {
    #[error(transparent)]
    LetterFreq(#[from] LetterFreqError),

    #[error(transparent)]
    Io(#[from] io::Error),
}

const ALLOW_WORD_REUSE: bool = false;

impl Solver {
    pub fn new<R: BufRead>(reader: R, phrase: &str) -> Result<Self, SolverError> {
        let (alphabet, target_freq) = Alphabet::from_phrase(phrase)?;

        let mut groups_map = HashMap::<LetterFreq, Vec<String>>::new();

        for line in reader.lines() {
            let line = line?;
            let line = line.trim();

            if let Some(freq) = alphabet.frequency_for(line) {
                if target_freq.contains(&freq) {
                    groups_map
                        .entry(freq)
                        .or_default()
                        .push(line.to_uppercase());
                }
            }
        }

        let mut groups: Vec<CandidateGroup> = groups_map
            .into_iter()
            .map(|(frequency, words)| {
                let word_len = frequency.len();

                CandidateGroup {
                    frequency,
                    words,
                    word_len,
                }
            })
            .collect();

        groups.sort_unstable_by(|a, b| b.word_len.cmp(&a.word_len));

        Ok(Self {
            groups,
            target_freq,
        })
    }

    pub fn for_each_solution<E, F>(&self, mut on_match: F) -> Result<(), E>
    where
        F: FnMut(&[&str]) -> Result<(), E>,
    {
        let mut target_freq = self.target_freq.clone();
        let mut path = Vec::new();
        self.solve_recursive(&self.groups, &mut target_freq, &mut path, &mut on_match)
    }

    fn solve_recursive<'a, E, F>(
        &'a self,
        groups: &'a [CandidateGroup],
        remaining: &mut LetterFreq,
        path: &mut Vec<&'a CandidateGroup>,
        on_match: &mut F,
    ) -> Result<(), E>
    where
        F: FnMut(&[&str]) -> Result<(), E>,
    {
        if remaining.is_empty() {
            let mut matched_words = Vec::with_capacity(path.len());
            let mut scratch = Vec::with_capacity(path.len());
            return Self::expand_and_emit(path, 0, 0, &mut matched_words, &mut scratch, on_match);
        }

        for (i, group) in groups.iter().enumerate() {
            if remaining.contains(&group.frequency) {
                path.push(group);

                let next_slice = if ALLOW_WORD_REUSE {
                    &groups[i..]
                } else {
                    &groups[i + 1..]
                };

                *remaining -= &group.frequency;
                self.solve_recursive(next_slice, remaining, path, on_match)?;
                *remaining += &group.frequency;

                path.pop();
            }
        }

        Ok(())
    }

    fn expand_and_emit<'a, E, F>(
        path: &[&'a CandidateGroup],
        depth: usize,
        min_word_idx: usize,
        matched_words: &mut Vec<&'a str>,
        scratch: &mut Vec<&'a str>,
        on_match: &mut F,
    ) -> Result<(), E>
    where
        F: FnMut(&[&str]) -> Result<(), E>,
    {
        if depth == path.len() {
            scratch.clear();
            scratch.extend_from_slice(matched_words);
            scratch.sort_unstable();
            return on_match(scratch);
        }

        let start_idx = if depth > 0 && std::ptr::eq(path[depth], path[depth - 1]) {
            min_word_idx
        } else {
            0
        };

        for (i, word) in path[depth].words.iter().enumerate().skip(start_idx) {
            matched_words.push(word.as_str());
            Self::expand_and_emit(path, depth + 1, i, matched_words, scratch, on_match)?;
            matched_words.pop();
        }

        Ok(())
    }
}
