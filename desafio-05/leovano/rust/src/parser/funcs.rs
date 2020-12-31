use super::{get_vecs, u8x32, VECTOR_QUOTE};
use crate::fields::{AreaCode, Salary, Text};

pub struct FuncsParser<'a> {
    text: &'a [u8],
    pos: usize,
    vec_quotes: u64,
    quotes_count: u32,
    is_done: bool,
}

impl<'a> FuncsParser<'a> {
    pub fn new(text: &'a [u8]) -> Self {
        let (vec_quotes, quotes_count, is_done) = get_vecs(text, 0);

        FuncsParser {
            text,
            pos: 0,
            vec_quotes,
            quotes_count,
            is_done,
        }
    }

    fn clear_bit(&mut self) -> usize {
        let result = self.vec_quotes.trailing_zeros();
        self.vec_quotes &= self.vec_quotes - 1;
        self.quotes_count -= 1;
        result as usize
    }

    pub fn is_done(&self) -> bool {
        self.quotes_count == 0 && self.is_done
    }

    pub fn replenish(&mut self) {
        self.pos += 64;
        let (vec_quotes, quotes_count, is_done) = get_vecs(self.text, self.pos);
        self.vec_quotes = vec_quotes;
        self.quotes_count = quotes_count;
        self.is_done = is_done;
    }

    pub fn skip_string(&mut self) -> (usize, usize) {
        let (lhs, rhs);
        if self.quotes_count == 0 {
            self.replenish();
            lhs = self.clear_bit();
            rhs = self.clear_bit();
        } else if self.quotes_count == 1 {
            lhs = 64 - self.clear_bit();
            self.replenish();
            rhs = self.clear_bit();
        } else {
            lhs = self.clear_bit();
            rhs = self.clear_bit();
        }

        (self.pos + lhs, self.pos + rhs)
    }

    pub fn get_string(&mut self) -> (Text<'a>, usize) {
        if self.quotes_count == 1 {
            let lhs = self.pos + self.clear_bit();
            self.replenish();
            let rhs = self.pos + self.clear_bit();

            (Text(&self.text[lhs + 1..rhs]), lhs)
        } else {
            if self.quotes_count == 0 {
                self.replenish();
            }

            let lhs = self.clear_bit();
            let rhs = self.clear_bit();

            (Text(&self.text[self.pos + lhs + 1..self.pos + rhs]), lhs)
        }
    }

    pub fn osp_get_salary(&mut self, mut idx: usize) -> Salary {
        let mut res = 0;

        if self.text[idx] == b' ' {
            idx += 1;
        }

        for &c in &self.text[idx..idx + 6] {
            if c != b'.' {
                debug_assert!(c.is_ascii_digit());
                res *= 10;
                res += u64::from(c - b'0');
                idx += 1;
            } else {
                break;
            }
        }

        res *= 100;
        res += u64::from(self.text[idx + 1] - b'0') * 10 + u64::from(self.text[idx + 2] - b'0');

        Salary::from(res)
    }

    pub fn osp_get_area(&mut self) -> AreaCode {
        if self.quotes_count == 0 {
            self.replenish();
        }

        let lhs = self.pos + self.clear_bit();

        if self.quotes_count == 0 {
            self.replenish();
        }

        self.clear_bit();
        AreaCode::from([self.text[lhs + 1], self.text[lhs + 2]])
    }
}
