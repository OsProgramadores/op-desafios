use std::fmt::{self, Debug, Display};
use std::ops::{Add, AddAssign, Div};

#[derive(Clone, Copy, Default, PartialEq, PartialOrd)]
pub struct Salary {
    inner: u64,
}

impl From<u64> for Salary {
    fn from(input: u64) -> Self {
        Salary { inner: input }
    }
}

impl Debug for Salary {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        Display::fmt(self, f)
    }
}

impl Display for Salary {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}.{:02}", self.inner / 100, self.inner % 100)
    }
}

impl Add for Salary {
    type Output = Salary;

    fn add(self, other: Salary) -> Salary {
        Salary::from(self.inner + other.inner)
    }
}

impl Div<u64> for Salary {
    type Output = Salary;

    fn div(self, other: u64) -> Salary {
        let mut res = self.inner / other;
        if self.inner % other > other / 2 {
            res += 1;
        }
        Salary::from(res)
    }
}

impl AddAssign for Salary {
    fn add_assign(&mut self, other: Salary) {
        self.inner += other.inner;
    }
}
