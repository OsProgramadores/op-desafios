use std::fmt;

pub struct Nome<'a>(&'a str, &'a str);

impl<'a> Nome<'a> {
    #[inline]
    pub fn new(nome: &'a str, sobrenome: &'a str) -> Nome<'a> {
        Nome(nome, sobrenome)
    }
}

impl<'a> fmt::Display for Nome<'a> {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} {}", self.0, self.1)
    }
}
