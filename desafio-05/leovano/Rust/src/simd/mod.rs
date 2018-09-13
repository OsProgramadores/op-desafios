mod avx;
mod types;

#[cfg(target_arch = "x86")]
use std::arch::x86::*;
#[cfg(target_arch = "x86_64")]
use std::arch::x86_64::*;

pub use self::types::{m8x32, u8x32};

extern "platform-intrinsic" {
    pub fn simd_eq<T, U>(x: T, y: T) -> U;
}
