use super::{Funcionario, Salary};
use std::sync::Arc;

// Stats: Global
#[derive(Debug, Default)]
pub struct GlobalStats<'a> {
    min: Salary,
    max: Salary,
    pub list_min: Vec<Arc<Funcionario<'a>>>,
    pub list_max: Vec<Arc<Funcionario<'a>>>,
    pub sum: Salary,
    pub count: u64,
}

impl<'a> GlobalStats<'a> {
    pub fn from_single(input: Arc<Funcionario<'a>>) -> Self {
        GlobalStats {
            min: input.salario,
            max: input.salario,
            sum: input.salario,
            list_min: vec![Arc::clone(&input)],
            list_max: vec![input],
            count: 1,
        }
    }

    pub fn from_duo(
        lhs: Arc<Funcionario<'a>>,
        rhs: Arc<Funcionario<'a>>,
    ) -> Self {
        GlobalStats {
            min: lhs.salario,
            max: rhs.salario,
            sum: lhs.salario + rhs.salario,
            list_min: vec![lhs],
            list_max: vec![rhs],
            count: 2,
        }
    }

    pub(super) fn update(&mut self, func: &Arc<Funcionario<'a>>) {
        if func.salario < self.min {
            self.min = func.salario;
            self.list_min.clear();
            self.list_min.push(Arc::clone(func));
        } else if func.salario > self.max {
            self.max = func.salario;
            self.list_max.clear();
            self.list_max.push(Arc::clone(func));
        } else if func.salario == self.min {
            self.list_min.push(Arc::clone(func));
        } else if func.salario == self.max {
            self.list_max.push(Arc::clone(func));
        }

        self.sum += func.salario;
        self.count += 1;
    }

    pub(super) fn merge(&mut self, mut other: GlobalStats<'a>) {
        if self.min > other.min {
            self.min = other.min;
            self.list_min = other.list_min;
        } else if self.min == other.min {
            self.list_min.append(&mut other.list_min);
        }

        if self.max < other.max {
            self.max = other.max;
            self.list_max = other.list_max;
        } else if self.max == other.max {
            self.list_max.append(&mut other.list_max);
        }

        self.sum += other.sum;
        self.count += other.count;
    }

    #[inline]
    pub fn average(&self) -> Salary {
        self.sum / self.count
    }
}
