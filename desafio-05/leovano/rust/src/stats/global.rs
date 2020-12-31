use super::{Aoc, Funcionario, Salary};

use std::sync::Arc;

#[derive(Debug)]
pub struct GlobalStats<'a> {
    pub min: Salary,
    pub max: Salary,
    pub list_min: Vec<Arc<Funcionario<'a>>>,
    pub list_max: Vec<Arc<Funcionario<'a>>>,
    pub sum: Salary,
    pub count: u64,
}

impl<'a> GlobalStats<'a> {
    pub fn new(input: &mut Aoc<Funcionario<'a>>) -> Self {
        GlobalStats {
            min: input.salario,
            max: input.salario,
            sum: input.salario,
            list_min: vec![Aoc::share(input)],
            list_max: vec![Aoc::share(input)],
            count: 1,
        }
    }

    pub(super) fn update(&mut self, func: &mut Aoc<Funcionario<'a>>) {
        if func.salario < self.min {
            self.min = func.salario;
            self.list_min.clear();
            self.list_min.push(Aoc::share(func));
        } else if func.salario > self.max {
            self.max = func.salario;
            self.list_max.clear();
            self.list_max.push(Aoc::share(func));
        } else if func.salario == self.min {
            self.list_min.push(Aoc::share(func));
        } else if func.salario == self.max {
            self.list_max.push(Aoc::share(func));
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

    pub fn average(&self) -> Salary {
        self.sum / self.count
    }
}
