use super::{Aoc, AreaCode, Entry, Funcionario, GlobalStats, Map, MapIter, Salary};

use std::sync::Arc;

// Stats: Specific
#[derive(Debug, Default)]
pub struct SpecStats<'a> {
    hash: Map<AreaCode, GlobalStats<'a>>,
}

impl<'a> SpecStats<'a> {
    pub(super) fn update(&mut self, func: &mut Aoc<Funcionario<'a>>) {
        match self.hash.entry(func.area) {
            Entry::Occupied(e) => e.into_mut().update(func),
            Entry::Vacant(e) => {
                e.insert(GlobalStats::new(func));
            }
        }
    }

    pub(super) fn merge(&mut self, other: SpecStats<'a>) {
        for (k, v) in other.hash {
            match self.hash.entry(k) {
                Entry::Occupied(e) => e.into_mut().merge(v),
                Entry::Vacant(e) => {
                    e.insert(v);
                }
            }
        }
    }

    pub fn iter(&self) -> MapIter<AreaCode, GlobalStats<'a>> {
        self.hash.iter()
    }

    pub fn average(&self, key: AreaCode) -> Salary {
        let res = &self.hash[&key];
        res.sum / res.count
    }
}
