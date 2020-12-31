use super::{get_vecs, u8x32, VECTOR_QUOTE};
use crate::fields::{Areas, Text};

pub struct AreasParser<'a> {
    text: &'a [u8],
    pos: usize,
    vec_quotes: u64,
    quotes_count: u32,
}

impl<'a> AreasParser<'a> {
    pub fn new(text: &'a [u8]) -> AreasParser<'a> {
        let pos = text.len() - 64;
        let (vec_quotes, quotes_count, _) = get_vecs(text, pos);

        AreasParser {
            text,
            pos,
            vec_quotes,
            quotes_count,
        }
    }

    fn replenish(&mut self) {
        self.pos -= 64;
        let (vec_quotes, quotes_count, _) = get_vecs(self.text, self.pos);
        self.vec_quotes = vec_quotes;
        self.quotes_count = quotes_count;
    }

    fn clear_bit(&mut self) -> usize {
        let result = 63 - self.vec_quotes.leading_zeros();
        self.vec_quotes ^= 1 << result;
        self.quotes_count -= 1;
        result as usize
    }

    pub fn skip_string(&mut self) -> usize {
        let result;
        if self.quotes_count == 0 {
            self.replenish();
            self.clear_bit();
            result = self.clear_bit();
        } else if self.quotes_count == 1 {
            self.replenish();
            result = self.clear_bit();
        } else {
            self.clear_bit();
            result = self.clear_bit();
        }

        result as usize
    }

    pub fn get_string(&mut self) -> (Text<'a>, usize) {
        if self.quotes_count == 1 {
            let snd = self.clear_bit();
            self.replenish();
            let fst = self.clear_bit();

            let slice = &self.text[self.pos + fst + 1..self.pos + snd + 64];
            (Text(slice), fst)
        } else {
            if self.quotes_count == 0 {
                self.replenish();
            }
            let snd = self.clear_bit();
            let fst = self.clear_bit();

            let slice = &self.text[self.pos + fst + 1..self.pos + snd];
            (Text(slice), fst)
        }
    }

    pub fn osp_rbracket(&mut self, mut max: usize) -> usize {
        if self.quotes_count == 0 {
            self.replenish();
            max += 64;
        }

        let min = self.pos + 63 - self.vec_quotes.leading_zeros() as usize;

        self.text[min..self.pos + max]
            .iter()
            .position(|&it| it == b']')
            .map(|it| min + it)
            .unwrap_or(0)
    }

    pub fn osp_get_area(&mut self) -> [u8; 2] {
        if self.quotes_count == 0 {
            self.replenish();
        }

        let snd = self.pos + self.clear_bit();

        if self.quotes_count == 0 {
            self.replenish();
        }

        self.clear_bit();
        [self.text[snd - 2], self.text[snd - 1]]
    }
}
