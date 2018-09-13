mod areacode;
mod areas;
mod nome;
mod salary;
pub use self::{
    areacode::AreaCode, //
    areas::Areas,
    nome::Nome,
    salary::Salary,
};

use stats::Stats;
use std::fmt;

pub struct Text<'a>(pub(crate) &'a [u8]);

impl<'a> fmt::Display for Text<'a> {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", unsafe { ::std::str::from_utf8_unchecked(self.0) })
    }
}

#[derive(Debug, Default)]
pub struct Empresa<'a> {
    pub stats: Stats<'a>,
    pub areas: Areas<'a>,
}

impl<'a> Empresa<'a> {
    pub(crate) fn new(stats: Stats<'a>, areas: Areas<'a>) -> Self {
        Empresa { stats, areas }
    }
}

pub struct Funcionario<'a> {
    nome: &'a [u8],
    pub(crate) sobrenome: &'a [u8],
    pub salario: Salary,
    pub(crate) area: AreaCode,
}

impl<'a> fmt::Debug for Funcionario<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.debug_struct("Funcionario")
            .field("nome", &self.nome())
            .field("salario", &self.salario)
            .field("area", &self.area)
            .finish()
    }
}

impl<'a> Funcionario<'a> {
    pub fn new(
        nome: &'a [u8],
        sobrenome: &'a [u8],
        salario: u64,
        area: [u8; 2],
    ) -> Self {
        Funcionario {
            nome,
            sobrenome,
            salario: Salary::from(salario),
            area: AreaCode::from(area),
        }
    }

    #[inline]
    pub fn nome(&self) -> Nome<'a> {
        Nome::new(self.nome, self.sobrenome)
    }
}
