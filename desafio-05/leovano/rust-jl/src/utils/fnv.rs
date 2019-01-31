use std::default::Default;
use std::hash::{BuildHasherDefault, Hasher};
use std::num::Wrapping;

pub struct FnvHasher(u64);

impl Default for FnvHasher {
    #[inline]
    fn default() -> FnvHasher {
        FnvHasher(0xcbf2_9ce4_8422_2325)
    }
}

impl Hasher for FnvHasher {
    #[inline]
    fn finish(&self) -> u64 {
        self.0
    }

    #[inline]
    fn write(&mut self, bytes: &[u8]) {
        let FnvHasher(hash) = *self;
        let mut hash = Wrapping(hash);

        for byte in bytes {
            hash ^= Wrapping(u64::from(*byte));
            hash *= Wrapping(0x0100_0000_01b3);
        }

        *self = FnvHasher(hash.0);
    }
}

pub type FnvBuildHasher = BuildHasherDefault<FnvHasher>;
