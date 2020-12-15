mod counter;
mod global;
mod max;
mod spec;
use self::{
    counter::CounterStats, //
    global::GlobalStats,
    max::MaxStats,
    spec::SpecStats,
};

use fields::{Funcionario, Salary};
use std::mem::swap;
use std::sync::Arc;
use utils::FnvBuildHasher;

use std::collections::hash_map::{Entry, HashMap, Iter};

type Map<K, V, H> = HashMap<K, V, H>;
type BuildHasher = FnvBuildHasher;
type MapIter<'a, K, V> = Iter<'a, K, V>;

#[derive(Debug, Default)]
pub struct Stats<'a> {
    pub global: GlobalStats<'a>,
    pub by_area: SpecStats<'a>,
    pub by_employees: CounterStats,
    pub by_lastname: MaxStats<'a>,
}

impl<'a> Stats<'a> {
    pub fn from_single(input: Funcionario<'a>) -> Self {
        let input = Arc::new(input);

        let mut by_area = SpecStats::default();
        by_area.update(&input);

        let mut by_employees = CounterStats::default();
        by_employees.update(&input);

        let mut by_lastname = MaxStats::default();
        by_lastname.update(&input);

        let global = GlobalStats::from_single(input);

        Stats {
            global,
            by_area,
            by_employees,
            by_lastname,
        }
    }

    pub fn from_duo(
        mut lhs: Funcionario<'a>,
        mut rhs: Funcionario<'a>,
    ) -> Self {
        if lhs.salario > rhs.salario {
            swap(&mut lhs, &mut rhs);
        }

        let lhs = Arc::new(lhs);
        let rhs = Arc::new(rhs);

        let mut by_area = SpecStats::default();
        by_area.update(&lhs);
        by_area.update(&rhs);

        let mut by_employees = CounterStats::default();
        by_employees.update(&lhs);
        by_employees.update(&rhs);

        let mut by_lastname = MaxStats::default();
        by_lastname.update(&lhs);
        by_lastname.update(&rhs);

        let global = GlobalStats::from_duo(lhs, rhs);
        Stats {
            global,
            by_area,
            by_employees,
            by_lastname,
        }
    }

    #[inline]
    pub fn update(&mut self, func: Funcionario<'a>) {
        let func = Arc::new(func);

        self.global.update(&func);
        self.by_area.update(&func);
        self.by_employees.update(&func);
        self.by_lastname.update(&func);
    }

    #[inline]
    pub fn merge(&mut self, other: Stats<'a>) {
        self.global.merge(other.global);
        self.by_area.merge(other.by_area);
        self.by_employees.merge(other.by_employees);
        self.by_lastname.merge(other.by_lastname);
    }
}
