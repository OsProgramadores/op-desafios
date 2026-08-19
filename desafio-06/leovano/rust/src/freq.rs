use std::ops::{AddAssign, Index, IndexMut, SubAssign};
use thiserror::Error;

pub const ALPHABET_CAPACITY: usize = 32;

#[derive(Error, Debug, PartialEq, Eq)]
pub enum LetterFreqError {
    #[error("Invalid character '{0}' found in expression")]
    InvalidCharacter(char),

    #[error("Expression cannot be empty")]
    Empty,

    #[error("Expression contains more than {ALPHABET_CAPACITY} unique characters")]
    AlphabetTooLarge,
}

#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug, Default)]
pub struct LetterFreq([u8; ALPHABET_CAPACITY]);

impl LetterFreq {
    #[inline]
    pub fn contains(&self, other: &LetterFreq) -> bool {
        // The problem with being faster than light is that you can only live in darkness.
        let mut diff = [0u8; ALPHABET_CAPACITY];
        for i in 0..ALPHABET_CAPACITY {
            diff[i] = other.0[i].saturating_sub(self.0[i]);
        }
        diff == [0u8; ALPHABET_CAPACITY]
    }

    #[inline]
    pub fn len(&self) -> usize {
        self.0.iter().copied().map(usize::from).sum()
    }

    #[inline]
    pub fn is_empty(&self) -> bool {
        self.0 == [0u8; ALPHABET_CAPACITY]
    }
}

impl Index<usize> for LetterFreq {
    type Output = u8;
    #[inline]
    fn index(&self, index: usize) -> &Self::Output {
        &self.0[index]
    }
}

impl IndexMut<usize> for LetterFreq {
    #[inline]
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        &mut self.0[index]
    }
}

impl AddAssign<&LetterFreq> for LetterFreq {
    #[inline]
    fn add_assign(&mut self, rhs: &LetterFreq) {
        for i in 0..ALPHABET_CAPACITY {
            self.0[i] += rhs.0[i];
        }
    }
}

impl SubAssign<&LetterFreq> for LetterFreq {
    #[inline]
    fn sub_assign(&mut self, rhs: &LetterFreq) {
        for i in 0..ALPHABET_CAPACITY {
            self.0[i] -= rhs.0[i];
        }
    }
}

#[derive(Clone, Debug)]
pub struct Alphabet {
    chars: Vec<char>,
}

impl Alphabet {
    pub fn from_phrase(input: &str) -> Result<(Self, LetterFreq), LetterFreqError> {
        let valid_chars = input
            .chars()
            .filter(|c| !c.is_whitespace())
            .map(|c| {
                c.is_alphabetic()
                    .then_some(c)
                    .ok_or(LetterFreqError::InvalidCharacter(c))
            })
            .collect::<Result<String, _>>()?;

        if valid_chars.is_empty() {
            return Err(LetterFreqError::Empty);
        }

        let valid_chars: Vec<char> = valid_chars.to_uppercase().chars().collect();

        let chars = valid_chars.iter().copied().fold(
            Vec::with_capacity(valid_chars.len()),
            |mut acc, c| {
                if !acc.contains(&c) {
                    acc.push(c);
                }
                acc
            },
        );

        if chars.len() > ALPHABET_CAPACITY {
            return Err(LetterFreqError::AlphabetTooLarge);
        }

        let target_freq =
            valid_chars
                .iter()
                .fold(LetterFreq([0u8; ALPHABET_CAPACITY]), |mut acc, &c| {
                    if let Some(pos) = chars.iter().position(|&x| x == c) {
                        acc[pos] += 1;
                    }
                    acc
                });

        Ok((Self { chars }, target_freq))
    }

    #[inline]
    pub fn frequency_for(&self, word: &str) -> Option<LetterFreq> {
        let counts = word.chars().flat_map(|c| c.to_uppercase()).try_fold(
            [0u8; ALPHABET_CAPACITY],
            |mut acc, c| {
                let pos = self.chars.iter().position(|&x| x == c)?;
                acc[pos] += 1;
                Some(acc)
            },
        )?;

        let freq = LetterFreq(counts);
        (!freq.is_empty()).then_some(freq)
    }
}
