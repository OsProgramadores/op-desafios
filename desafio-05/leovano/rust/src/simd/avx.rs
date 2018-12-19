use super::*;

use std::mem;

cfg_if! {
    if #[cfg(target_feature = "avx2")] {
        #[inline]
        pub fn mm256_movemask_epi8(a: u8x32) -> i32 {
            unsafe { _mm256_movemask_epi8(mem::transmute(a)) }
        }
    } else if #[cfg(target_feature = "sse2")]  {
        #[inline]
        pub fn mm256_movemask_epi8(a: u8x32) -> i32 {
            unsafe {
                let a: [__m128i; 2] = mem::transmute(a);
                let lhs = _mm_movemask_epi8(a[0]) as i16;
                let rhs = _mm_movemask_epi8(a[1]) as i16;
                mem::transmute([lhs, rhs])
            }
        }
    }
}
