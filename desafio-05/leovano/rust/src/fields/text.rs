use std::cmp::{Eq, PartialEq};
use std::fmt::{self, Debug, Display};
use std::hash::Hash;

#[derive(Clone, Copy, Hash)]
pub struct Text<'a>(pub &'a [u8]);

impl<'a> Debug for Text<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", unsafe {
            ::std::str::from_utf8_unchecked(self.0)
        })
    }
}

impl<'a> Display for Text<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", unsafe { ::std::str::from_utf8_unchecked(self.0) })
    }
}

impl<'a> PartialEq for Text<'a> {
    fn eq(&self, other: &Text<'a>) -> bool {
        self.0 == other.0
    }
}

impl<'a, T: AsRef<[u8]>> PartialEq<T> for Text<'a> {
    fn eq(&self, other: &T) -> bool {
        self.0 == other.as_ref()
    }
}

impl<'a> Eq for Text<'a> {}
