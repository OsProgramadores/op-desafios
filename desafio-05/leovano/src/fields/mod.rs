mod areacode;
mod areas;
mod salary;
pub use self::areacode::AreaCode;
pub use self::areas::Areas;
pub use self::salary::{Salary, Sum};

use misc::Nome;

#[derive(Debug, Deserialize, Default)]
pub struct Empresa<'a> {
    #[serde(borrow)]
    pub funcionarios: Vec<Funcionario<'a>>,
    pub areas: Areas,
}

#[derive(Debug, Deserialize, Default)]
pub struct Funcionario<'a> {
    id: u64,
    nome: &'a str,
    pub sobrenome: &'a str,
    pub salario: Salary,
    pub area: AreaCode,
}

impl<'a> Funcionario<'a> {
    #[inline]
    pub fn nome(&self) -> Nome<'a> {
        Nome::new(self.nome, self.sobrenome)
    }
}
