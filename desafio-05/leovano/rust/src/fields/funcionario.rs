use super::{AreaCode, Nome, Salary, Text};
use std::fmt::{self, Debug, Display};

pub struct Funcionario<'a> {
    pub nome: Nome<'a>,
    pub salario: Salary,
    pub area: AreaCode,
}

impl<'a> Debug for Funcionario<'a> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.debug_struct("Funcionario")
            .field("nome", &self.nome)
            .field("salario", &self.salario)
            .field("area", &self.area)
            .finish()
    }
}

impl<'a> Funcionario<'a> {
    pub fn new(nome: Text<'a>, sobrenome: Text<'a>, salario: Salary, area: AreaCode) -> Self {
        let nome = Nome::new(nome, sobrenome);
        Funcionario {
            nome,
            salario,
            area,
        }
    }
}
