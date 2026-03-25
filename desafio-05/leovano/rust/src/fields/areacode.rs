use std::fmt;

#[derive(Clone, Copy, Hash, PartialEq)]
pub struct AreaCode {
    inner: [u8; 2],
}

impl fmt::Debug for AreaCode {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}{}", self.inner[0] as char, self.inner[1] as char)
    }
}

impl Eq for AreaCode {}

impl From<[u8; 2]> for AreaCode {
    #[inline]
    fn from(input: [u8; 2]) -> Self {
        AreaCode { inner: input }
    }
}
