use fields::{AreaCode, Funcionario, Salary, Sum};
use fnv::FnvBuildHasher;
use indexmap::{map::Iter, IndexMap};
use std::fmt::Debug;
use std::hash::Hash;
use std::mem;

// Stats
#[derive(Debug)]
pub struct Stats<'a> {
    pub global: GlobalStats<'a>,
    pub by_area: SpecStats<'a, AreaCode>,
    pub by_employees: CounterStats<'a, AreaCode>,
    pub by_lastname: MaxStats<'a, &'a str>,
}

impl<'a> Stats<'a> {
    pub fn from_single(input: &'a Funcionario<'a>) -> Self {
        let global = GlobalStats::from_single(input);

        let mut by_area = SpecStats::new();
        by_area.update(input, |it| &it.area);

        let mut by_employees = CounterStats::new();
        by_employees.update(input, |it| &it.area);

        let mut by_lastname = MaxStats::new();
        by_lastname.update(input, |it| &it.sobrenome);

        Stats {
            global,
            by_area,
            by_employees,
            by_lastname,
        }
    }

    pub fn from_duo(mut lhs: &'a Funcionario<'a>, mut rhs: &'a Funcionario<'a>) -> Self {
        if lhs.salario > rhs.salario {
            mem::swap(&mut lhs, &mut rhs);
        }

        let mut by_area = SpecStats::new();
        by_area.update(lhs, |it| &it.area);
        by_area.update(rhs, |it| &it.area);

        let mut by_employees = CounterStats::new();
        by_employees.update(lhs, |it| &it.area);
        by_employees.update(rhs, |it| &it.area);

        let mut by_lastname = MaxStats::new();
        by_lastname.update(lhs, |it| &it.sobrenome);
        by_lastname.update(rhs, |it| &it.sobrenome);

        let global = GlobalStats::from_duo(lhs, rhs);
        Stats {
            global,
            by_area,
            by_employees,
            by_lastname,
        }
    }

    #[inline]
    pub fn update(&mut self, func: &'a Funcionario<'a>) {
        self.global.update(func);
        self.by_area.update(func, |it| &it.area);
        self.by_employees.update(func, |it| &it.area);
        self.by_lastname.update(func, |it| &it.sobrenome);
    }
}

// Stats: Global
#[derive(Debug)]
pub struct GlobalStats<'a> {
    min: Salary,
    max: Salary,
    pub list_min: Vec<&'a Funcionario<'a>>,
    pub list_max: Vec<&'a Funcionario<'a>>,
    sum: Sum,
    count: usize,
}

impl<'a> GlobalStats<'a> {
    pub fn from_single(input: &'a Funcionario<'a>) -> Self {
        GlobalStats {
            min: input.salario.clone(),
            max: input.salario.clone(),
            list_min: vec![input],
            list_max: vec![input],
            sum: (&input.salario).into(),
            count: 1,
        }
    }

    pub fn from_duo(lhs: &'a Funcionario<'a>, rhs: &'a Funcionario<'a>) -> Self {
        GlobalStats {
            min: lhs.salario.clone(),
            max: rhs.salario.clone(),
            list_min: vec![lhs],
            list_max: vec![rhs],
            sum: &lhs.salario + &rhs.salario,
            count: 2,
        }
    }

    pub fn update(&mut self, func: &'a Funcionario<'a>) {
        if func.salario == self.min {
            self.list_min.push(func);
        } else if func.salario < self.min {
            self.min = func.salario.clone();
            self.list_min.clear();
            self.list_min.push(func);
        } else if func.salario == self.max {
            self.list_max.push(func);
        } else if func.salario > self.max {
            self.max = func.salario.clone();
            self.list_max.clear();
            self.list_max.push(func);
        }

        self.sum += &func.salario;
        self.count += 1;
    }

    #[inline]
    pub fn average(&self) -> Sum {
        self.sum.average(self.count)
    }
}

// Stats: Specific
#[derive(Debug)]
pub struct SpecStats<'a, T: 'a>
where
    T: Debug + Hash + Eq,
{
    hash: IndexMap<&'a T, GlobalStats<'a>, FnvBuildHasher>,
}

impl<'a, T: 'a> SpecStats<'a, T>
where
    T: Debug + Hash + Eq,
{
    fn new() -> Self {
        SpecStats {
            hash: IndexMap::default(),
        }
    }

    fn update<F>(&mut self, func: &'a Funcionario<'a>, cmp: F)
    where
        F: Fn(&'a Funcionario<'a>) -> &'a T,
    {
        use indexmap::map::Entry;

        match self.hash.entry(cmp(func)) {
            Entry::Occupied(e) => e.into_mut().update(func),
            Entry::Vacant(e) => {
                e.insert(GlobalStats::from_single(func));
            }
        }
    }

    #[inline]
    pub fn iter(&self) -> Iter<&'a T, GlobalStats<'a>> {
        self.hash.iter()
    }

    #[inline]
    pub fn average(&self, key: &T) -> Sum {
        let res = &self.hash[key];
        res.sum.average(res.count)
    }
}

// Alias: Counter->MinMax
type MinMax<'a, T> = ((Vec<&'a T>, usize), (Vec<&'a T>, usize));

// Stats: Counter
#[derive(Debug)]
pub struct CounterStats<'a, T: 'a>
where
    T: Debug + Hash + Eq,
{
    hash: IndexMap<&'a T, usize, FnvBuildHasher>,
}

impl<'a, T: 'a> CounterStats<'a, T>
where
    T: Debug + Hash + Eq,
{
    fn new() -> Self {
        CounterStats {
            hash: IndexMap::default(),
        }
    }

    fn update<F>(&mut self, func: &'a Funcionario<'a>, cmp: F)
    where
        F: Fn(&'a Funcionario<'a>) -> &'a T,
    {
        *self.hash.entry(cmp(func)).or_insert(0) += 1;
    }

    pub fn minmax(self) -> MinMax<'a, T> {
        let mut hash = self.hash.into_iter();

        let (mut min, mut max, mut list_min, mut list_max) = {
            let fst = hash.next().unwrap();
            let snd = hash.next().unwrap();

            if fst.1 > snd.1 {
                (snd.1, fst.1, vec![snd.0], vec![fst.0])
            } else {
                (fst.1, snd.1, vec![fst.0], vec![snd.0])
            }
        };

        for (s, c) in hash {
            if c == min {
                list_min.push(s);
            } else if c < min {
                min = c;
                list_min.clear();
                list_min.push(s);
            } else if c == max {
                list_max.push(s);
            } else if c > max {
                max = c;
                list_max.clear();
                list_max.push(s);
            }
        }

        ((list_min, min), (list_max, max))
    }
}

// Alias: MaxStats->Iter
#[allow(dead_code)]
type MaxIter<'a, T> = (&'a T, (&'a Salary, Vec<&'a Funcionario<'a>>));

// Stats: Max
#[derive(Debug)]
pub struct MaxStats<'a, T: 'a>
where
    T: Debug + Hash + Eq,
{
    hash: IndexMap<&'a T, (usize, &'a Salary, Vec<&'a Funcionario<'a>>), FnvBuildHasher>,
}

impl<'a, T: 'a> MaxStats<'a, T>
where
    T: Debug + Hash + Eq,
{
    fn new() -> Self {
        MaxStats {
            hash: IndexMap::default(),
        }
    }

    fn update<F>(&mut self, func: &'a Funcionario<'a>, cmp: F)
    where
        F: Fn(&'a Funcionario<'a>) -> &'a T,
    {
        use indexmap::map::Entry;

        match self.hash.entry(cmp(func)) {
            Entry::Occupied(e) => {
                let e = e.into_mut();
                e.0 += 1;
                if e.1 == &func.salario {
                    e.2.push(func);
                } else if e.1 < &func.salario {
                    e.2.clear();
                    e.2.push(func);
                    e.1 = &func.salario;
                }
            }
            Entry::Vacant(e) => {
                e.insert((1, &func.salario, vec![func]));
            }
        }
    }

    pub fn into_iter(self) -> impl Iterator<Item = MaxIter<'a, T>> {
        self.hash
            .into_iter()
            .filter(|(_, it)| it.0 > 1)
            .map(|(a, (_, b, c))| (a, (b, c)))
    }
}
