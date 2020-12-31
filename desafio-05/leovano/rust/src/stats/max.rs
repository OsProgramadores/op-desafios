use super::{Aoc, Entry, Funcionario, Map, Salary, Text};

use std::sync::Arc;

// MaxStats->Data
#[derive(Debug)]
struct MaxStatsData<'a> {
    pub count: usize,
    pub salary: Salary,
    pub list: Vec<Arc<Funcionario<'a>>>,
}

// MaxStats->Iter
#[derive(Debug)]
pub struct MaxStatsIter<'a> {
    pub surname: Text<'a>,
    pub salary: Salary,
    pub list: Vec<Arc<Funcionario<'a>>>,
}

// Stats: Max
#[derive(Debug, Default)]
pub struct MaxStats<'a> {
    hash: Map<Text<'a>, MaxStatsData<'a>>,
}

impl<'a> MaxStats<'a> {
    pub(super) fn update(&mut self, func: &mut Aoc<Funcionario<'a>>) {
        match self.hash.entry(*func.nome.surname()) {
            Entry::Occupied(e) => {
                let e = e.into_mut();
                e.count += 1;
                if e.salary < func.salario {
                    e.salary = func.salario;
                    e.list.clear();
                    e.list.push(Aoc::share(func));
                } else if e.salary == func.salario {
                    e.list.push(Aoc::share(func));
                }
            }
            Entry::Vacant(e) => {
                e.insert(MaxStatsData {
                    count: 1,
                    salary: func.salario,
                    list: vec![Aoc::share(func)],
                });
            }
        }
    }

    pub(super) fn merge(&mut self, other: MaxStats<'a>) {
        for (k, mut v) in other.hash {
            match self.hash.entry(k) {
                Entry::Occupied(e) => {
                    let e = e.into_mut();
                    e.count += v.count;
                    if e.salary < v.salary {
                        e.salary = v.salary;
                        e.list = v.list;
                    } else if e.salary == v.salary {
                        e.list.append(&mut v.list);
                    }
                }
                Entry::Vacant(e) => {
                    e.insert(v);
                }
            }
        }
    }

    pub fn into_iter(self) -> impl Iterator<Item = MaxStatsIter<'a>> {
        self.hash
            .into_iter()
            .filter(|(_, it)| it.count > 1)
            .map(|(surname, data)| MaxStatsIter {
                surname,
                salary: data.salary,
                list: data.list,
            })
    }
}
