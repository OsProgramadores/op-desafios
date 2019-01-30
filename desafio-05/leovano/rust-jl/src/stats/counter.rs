use super::Funcionario;
use super::{BuildHasher, Map};

use fields::AreaCode;
use std::sync::Arc;

// Alias: Counter->MinMax
type MinMax = ((Vec<AreaCode>, usize), (Vec<AreaCode>, usize));

// Stats: Counter
#[derive(Debug, Default)]
pub struct CounterStats {
    hash: Map<AreaCode, usize, BuildHasher>,
}

impl CounterStats {
    #[inline]
    pub(super) fn update<'a>(&mut self, func: &Arc<Funcionario<'a>>) {
        *self.hash.entry(func.area).or_insert(0) += 1;
    }

    #[inline]
    pub(super) fn merge(&mut self, other: CounterStats) {
        for (k, v) in other.hash {
            *self.hash.entry(k).or_insert(0) += v;
        }
    }

    #[inline]
    pub fn minmax(self) -> MinMax {
        let mut hash = self.hash.into_iter();

        let (mut min, mut max, mut list_min, mut list_max) = {
            let fst = hash.next().unwrap();

            if let Some(snd) = hash.next() {
                if fst.1 > snd.1 {
                    (snd.1, fst.1, vec![snd.0], vec![fst.0])
                } else {
                    (fst.1, snd.1, vec![fst.0], vec![snd.0])
                }
            } else {
                return ((vec![fst.0], fst.1), (vec![fst.0], fst.1));
            }
        };

        for (s, c) in hash {
            if c < min {
                min = c;
                list_min.clear();
                list_min.push(s);
            } else if c > max {
                max = c;
                list_max.clear();
                list_max.push(s);
            } else if c == min {
                list_min.push(s);
            } else if c == max {
                list_max.push(s);
            }
        }

        ((list_min, min), (list_max, max))
    }
}
