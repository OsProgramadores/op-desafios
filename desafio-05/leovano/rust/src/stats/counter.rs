use super::{Aoc, AreaCode, Funcionario, Map};

use std::cmp::Ordering;

// Counter->MinMax
pub struct CounterStatsMinMax {
    pub min: usize,
    pub max: usize,
    pub list_min: Vec<AreaCode>,
    pub list_max: Vec<AreaCode>,
}

// Stats: Counter
#[derive(Debug, Default)]
pub struct CounterStats {
    hash: Map<AreaCode, usize>,
}

impl CounterStats {
    pub(super) fn update<'a>(&mut self, func: &Aoc<Funcionario<'a>>) {
        *self.hash.entry(func.area).or_insert(0) += 1;
    }

    pub(super) fn merge(&mut self, other: CounterStats) {
        for (k, v) in other.hash {
            *self.hash.entry(k).or_insert(0) += v;
        }
    }

    pub fn minmax(self) -> CounterStatsMinMax {
        let size = self.hash.len();
        let mut hash = self.hash.into_iter();

        if size == 0 {
            unreachable!("entry must contain at least one employee");
        }

        let fst = hash.next().unwrap();
        let mut mm = CounterStatsMinMax {
            min: fst.1,
            max: fst.1,
            list_min: vec![fst.0],
            list_max: vec![fst.0],
        };

        for (stats, count) in hash {
            if count < mm.min {
                mm.min = count;
                mm.list_min.clear();
                mm.list_min.push(stats);
            } else if count > mm.max {
                mm.max = count;
                mm.list_max.clear();
                mm.list_max.push(stats);
            } else if count == mm.min {
                mm.list_min.push(stats);
            } else if count == mm.max {
                mm.list_max.push(stats);
            }
        }

        mm
    }
}
