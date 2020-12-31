use super::Text;
use std::fmt::{self, Debug, Display};

pub struct Nome<'a>(Text<'a>, Text<'a>);

impl<'a> Nome<'a> {
    pub fn new(nome: Text<'a>, sobrenome: Text<'a>) -> Nome<'a> {
        Nome(nome, sobrenome)
    }

    pub fn surname(&self) -> &Text<'a> {
        &self.1
    }
}

impl<'a> Debug for Nome<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?} {:?}", self.0, self.1)
    }
}

impl<'a> Display for Nome<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} {}", self.0, self.1)
    }
}
