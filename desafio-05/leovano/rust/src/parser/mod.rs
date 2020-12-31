mod areas;
mod funcs;
pub use areas::AreasParser;
pub use funcs::FuncsParser;

use crate::simd::u8x32;

const VECTOR_QUOTE: u8x32 = u8x32::splat(b'"');

fn join_u64(lhs: u32, rhs: u32) -> u64 {
    u64::from(rhs.to_le()) << 32 | u64::from(lhs.to_le())
}

fn get_vecs(text: &[u8], pos: usize) -> (u64, u32, bool) {
    let (v1, v2, is_done);

    if pos + 64 <= text.len() {
        v1 = u8x32::from(&text[pos..pos + 32]);
        v2 = u8x32::from(&text[pos + 32..pos + 64]);
        is_done = pos + 64 == text.len();
    } else if pos + 32 <= text.len() {
        v1 = u8x32::from(&text[pos..pos + 32]);
        v2 = u8x32::from(&text[pos + 32..]);
        is_done = true;
    } else {
        v1 = u8x32::from(&text[pos..]);
        v2 = u8x32::default();
        is_done = true;
    }

    let s1 = v1.eq(VECTOR_QUOTE).movemask();
    let s2 = v2.eq(VECTOR_QUOTE).movemask();
    let vec_quotes = join_u64(s1, s2);
    let quotes_count = vec_quotes.count_ones();

    (vec_quotes, quotes_count, is_done)
}
