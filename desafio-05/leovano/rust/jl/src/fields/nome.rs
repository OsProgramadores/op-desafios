use super::Text;
use std::fmt;

pub struct Nome<'a>(Text<'a>, Text<'a>);

impl<'a> Nome<'a> {
    #[inline]
    pub fn new(nome: &'a [u8], sobrenome: &'a [u8]) -> Nome<'a> {
        Nome(Text(nome), Text(sobrenome))
    }
}

impl<'a> fmt::Debug for Nome<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self)
    }
}

impl<'a> fmt::Display for Nome<'a> {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} {}", self.0, self.1)
    }
}
