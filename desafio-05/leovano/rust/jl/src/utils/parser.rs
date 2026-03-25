use u8x32;

const VECTOR_QUOTE: u8x32 = u8x32::splat(b'"');
const VECTOR_CLOSE: u8x32 = u8x32::splat(b']');

#[inline]
fn join_u64(lhs: u32, rhs: u32) -> u64 {
    unsafe { ::std::mem::transmute([lhs, rhs]) }
}

pub struct Parser<'a> {
    text: &'a [u8],
    pos: usize,
    vec_bytes: (u8x32, u8x32),
    vec_quotes: u64,
    quotes_count: u32,
}

impl<'a> Parser<'a> {
    pub fn new(text: &'a [u8]) -> Self {
        let v1 = u8x32::from(&text[0..32]);
        let v2 = u8x32::from(&text[32..64]);
        let s1 = v1.eq(VECTOR_QUOTE).movemask();
        let s2 = v2.eq(VECTOR_QUOTE).movemask();
        let vec_quotes = join_u64(s1, s2);
        let quotes_count = vec_quotes.count_ones();
        let vec_bytes = (v1, v2);

        Parser {
            text,
            pos: 0,
            vec_bytes,
            vec_quotes,
            quotes_count,
        }
    }

    fn get_vecs(&mut self) {
        let (text, pos) = (&self.text, self.pos);

        if pos + 64 < text.len() {
            self.vec_bytes.0 = u8x32::from(&text[pos..pos + 32]);
            self.vec_bytes.1 = u8x32::from(&text[pos + 32..pos + 64]);
        } else if pos + 32 < text.len() {
            self.vec_bytes.0 = u8x32::from(&text[pos..pos + 32]);
            self.vec_bytes.1 = u8x32::from(&text[pos + 32..]);
        } else {
            self.vec_bytes.0 = u8x32::from(&text[pos..]);
            self.vec_bytes.1 = u8x32::default();
        }
    }

    #[inline]
    fn clear_bits(&mut self, n: u32) {
        for _ in 0..n {
            self.vec_quotes &= self.vec_quotes - 1;
        }
        self.quotes_count -= n;
    }

    fn read(&mut self) {
        self.pos += 64;
        self.get_vecs();
        let (v1, v2) = self.vec_bytes;

        let s1 = v1.eq(VECTOR_QUOTE).movemask();
        let s2 = v2.eq(VECTOR_QUOTE).movemask();

        self.vec_quotes = join_u64(s1, s2);
        self.quotes_count = self.vec_quotes.count_ones();
    }

    #[inline]
    pub fn is_done(&self) -> bool {
        self.quotes_count == 0 && self.pos + 64 >= self.text.len()
    }

    pub fn skip_string(&mut self) -> usize {
        let res;
        if self.quotes_count == 0 {
            self.read();
            self.vec_quotes &= self.vec_quotes - 1;
            res = self.vec_quotes.trailing_zeros();
            self.vec_quotes &= self.vec_quotes - 1;
            self.quotes_count -= 2;
        } else if self.quotes_count == 1 {
            self.read();
            res = self.vec_quotes.trailing_zeros();
            self.clear_bits(1);
        } else {
            self.vec_quotes &= self.vec_quotes - 1;
            res = self.vec_quotes.trailing_zeros();
            self.vec_quotes &= self.vec_quotes - 1;
            self.quotes_count -= 2;
        }

        res as usize
    }

    pub fn get_string(&mut self) -> &'a [u8] {
        if self.quotes_count == 1 {
            let pos = self.pos;
            let fst = self.vec_quotes.trailing_zeros() as usize;
            self.read();
            let snd = self.vec_quotes.trailing_zeros() as usize;
            self.clear_bits(1);
            &self.text[pos + fst + 1..pos + 64 + snd]
        } else {
            if self.quotes_count == 0 {
                self.read()
            }

            let pos = self.pos;
            let quotes = &mut self.vec_quotes;
            let fst = quotes.trailing_zeros() as usize;
            *quotes &= *quotes - 1;
            let snd = quotes.trailing_zeros() as usize;
            *quotes &= *quotes - 1;

            self.quotes_count -= 2;
            &self.text[pos + fst + 1..pos + snd]
        }
    }

    pub fn osp_rbracket(&mut self) -> usize {
        let (v1, v2) = self.vec_bytes;

        let s1 = v1.eq(VECTOR_CLOSE).movemask();
        let s2 = v2.eq(VECTOR_CLOSE).movemask();

        let res = join_u64(s1, s2).trailing_zeros();
        if self.quotes_count == 0 && res == 64 {
            self.read();

            let (v1, v2) = self.vec_bytes;

            let s1 = v1.eq(VECTOR_CLOSE).movemask();
            let s2 = v2.eq(VECTOR_CLOSE).movemask();

            join_u64(s1, s2).trailing_zeros() as usize
        } else {
            res as usize
        }
    }

    pub fn osp_get_salary(&mut self, numpos: usize) -> u32 {
        let mut res = 0;
        let pos = self.pos;

        let mut numpos = pos + numpos;
        for c in &self.text[numpos..numpos + 6] {
            if *c != b'.' {
                res *= 10;
                res += u32::from(*c - b'0');
                numpos += 1;
            } else {
                break;
            }
        }

        res *= 100;
        res += u32::from(self.text[numpos + 1] - b'0') * 10
            + u32::from(self.text[numpos + 2] - b'0');

        res
    }

    pub fn osp_get_area(&mut self) -> [u8; 2] {
        if self.quotes_count == 0 {
            self.read();
        }

        let fst = self.vec_quotes.trailing_zeros() as usize + self.pos;

        if self.quotes_count == 1 {
            self.read();
            self.clear_bits(1);
        } else {
            self.clear_bits(2);
        }

        [self.text[fst + 1], self.text[fst + 2]]
    }
}
