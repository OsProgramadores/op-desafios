use super::{BuildHasher, Entry, Map};
use super::{Funcionario, Salary};
use fields::Text;

use std::sync::Arc;

// Alias: MaxStats->Data
#[allow(dead_code)]
type MaxData<'a> = (usize, Salary, Vec<Arc<Funcionario<'a>>>);

// Alias: MaxStats->Iter
#[allow(dead_code)]
type MaxIter<'a> = (Text<'a>, Salary, Vec<Arc<Funcionario<'a>>>);

// Stats: Max
#[derive(Debug, Default)]
pub struct MaxStats<'a> {
    hash: Map<&'a [u8], MaxData<'a>, BuildHasher>,
}

impl<'a> MaxStats<'a> {
    pub(super) fn update(&mut self, func: &Arc<Funcionario<'a>>) {
        match self.hash.entry(func.sobrenome) {
            Entry::Occupied(e) => {
                let e = e.into_mut();
                e.0 += 1;
                if e.1 < func.salario {
                    e.2.clear();
                    e.1 = func.salario;
                    e.2.push(Arc::clone(func));
                } else if e.1 == func.salario {
                    e.2.push(Arc::clone(func));
                }
            }
            Entry::Vacant(e) => {
                e.insert((1, func.salario, vec![Arc::clone(func)]));
            }
        }
    }

    pub(super) fn merge(&mut self, other: MaxStats<'a>) {
        for (k, mut v) in other.hash {
            match self.hash.entry(k) {
                Entry::Occupied(e) => {
                    let e = e.into_mut();
                    e.0 += v.0;
                    if e.1 < v.1 {
                        e.1 = v.1;
                        e.2 = v.2;
                    } else if e.1 == v.1 {
                        e.2.append(&mut v.2);
                    }
                }
                Entry::Vacant(e) => {
                    e.insert(v);
                }
            }
        }
    }

    #[inline]
    pub fn into_iter(self) -> impl Iterator<Item = MaxIter<'a>> {
        self.hash
            .into_iter()
            .filter(|(_, it)| it.0 > 1)
            .map(|(ln, (_, b, c))| (Text(ln), b, c))
    }
}
