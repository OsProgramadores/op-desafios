use super::avx::*;
use super::simd_eq;
use std::ptr;

#[allow(non_camel_case_types)]
#[derive(Default, Clone, Copy)]
#[repr(simd)]
#[rustfmt::skip]
pub struct u8x32(
    u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8,
    u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8,
);

#[allow(non_camel_case_types)]
#[derive(Default, Clone, Copy)]
#[repr(simd)]
pub struct m8x32(u32, u32, u32, u32, u32, u32, u32, u32);

impl u8x32 {
    #[rustfmt::skip]
    pub const fn splat(it: u8) -> Self {
        u8x32(
            it, it, it, it, it, it, it, it, it, it, it, it, it, it, it, it,
            it, it, it, it, it, it, it, it, it, it, it, it, it, it, it, it,
        )
    }

    pub fn eq(&self, other: u8x32) -> u8x32 {
        unsafe { simd_eq(*self, other) }
    }

    pub fn movemask(&self) -> u32 {
        mm256_movemask_epi8(*self) as u32
    }
}

impl<'a> From<&'a [u8]> for u8x32 {
    fn from(value: &'a [u8]) -> Self {
        let len = value.len();
        assert!(len <= 32, "slice length cannot be greater than 32");
        let mut result = u8x32::default();

        unsafe {
            let vptr = value.get_unchecked(0) as *const u8;
            let rptr = &mut result as *mut Self as *mut u8;
            ptr::copy_nonoverlapping(vptr, rptr, len);
        }

        result
    }
}
