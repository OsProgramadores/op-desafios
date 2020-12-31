mod areacode;
mod areas;
mod funcionario;
mod nome;
mod salary;
mod text;
pub use self::{
    areacode::AreaCode, areas::Areas, funcionario::Funcionario, nome::Nome, salary::Salary,
    text::Text,
};

use crate::stats::Stats;

#[derive(Debug)]
pub struct Empresa<'a> {
    pub stats: Stats<'a>,
    pub areas: Areas<'a>,
}

impl<'a> Empresa<'a> {
    pub(crate) fn new(stats: Stats<'a>, areas: Areas<'a>) -> Self {
        Empresa { stats, areas }
    }
}
