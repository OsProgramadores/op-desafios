mod counter;
mod global;
mod max;
mod spec;
use self::{counter::CounterStats, global::GlobalStats, max::MaxStats, spec::SpecStats};

use crate::fields::{AreaCode, Funcionario, Salary, Text};
use crate::utils::Aoc;

// use std::collections::hash_map::{Entry, HashMap, Iter};
use hashbrown::hash_map::{Entry, Iter};
use hashbrown::HashMap;
use std::sync::Arc;

type Map<K, V> = HashMap<K, V, BuildHasher>;
type BuildHasher = fnv::FnvBuildHasher;
type MapIter<'a, K, V> = Iter<'a, K, V>;

#[derive(Debug)]
pub struct Stats<'a> {
    pub global: GlobalStats<'a>,
    pub by_area: SpecStats<'a>,
    pub by_employees: CounterStats,
    pub by_lastname: MaxStats<'a>,
}

impl<'a> Stats<'a> {
    pub fn new(func: Funcionario<'a>) -> Self {
        let mut func = Aoc::new(func);

        let mut by_area = SpecStats::default();
        by_area.update(&mut func);

        let mut by_employees = CounterStats::default();
        by_employees.update(&func);

        let mut by_lastname = MaxStats::default();
        by_lastname.update(&mut func);

        let global = GlobalStats::new(&mut func);

        Stats {
            global,
            by_area,
            by_employees,
            by_lastname,
        }
    }

    pub fn update(&mut self, mut func: Aoc<Funcionario<'a>>) {
        self.global.update(&mut func);
        self.by_area.update(&mut func);
        self.by_employees.update(&func);
        self.by_lastname.update(&mut func);
    }

    pub fn merge(&mut self, other: Stats<'a>) {
        self.global.merge(other.global);
        self.by_area.merge(other.by_area);
        self.by_employees.merge(other.by_employees);
        self.by_lastname.merge(other.by_lastname);
    }
}
