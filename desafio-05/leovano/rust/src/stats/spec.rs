use super::GlobalStats;
use super::{BuildHasher, Entry, Map, MapIter};
use super::{Funcionario, Salary};

use fields::AreaCode;
use std::sync::Arc;

// Stats: Specific
#[derive(Debug, Default)]
pub struct SpecStats<'a> {
    hash: Map<AreaCode, GlobalStats<'a>, BuildHasher>,
}

impl<'a> SpecStats<'a> {
    pub(super) fn update(&mut self, func: &Arc<Funcionario<'a>>) {
        match self.hash.entry(func.area) {
            Entry::Occupied(e) => e.into_mut().update(func),
            Entry::Vacant(e) => {
                e.insert(GlobalStats::from_single(Arc::clone(func)));
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

    #[inline]
    pub fn iter(&self) -> MapIter<AreaCode, GlobalStats<'a>> {
        self.hash.iter()
    }

    #[inline]
    pub fn average(&self, key: AreaCode) -> Salary {
        let res = &self.hash[&key];
        res.sum / res.count
    }
}
