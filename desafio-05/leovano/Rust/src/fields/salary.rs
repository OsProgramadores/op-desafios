use std::fmt;
use std::ops::{Add, AddAssign, Div};

#[derive(Clone, Copy, Default, PartialEq, PartialOrd)]
pub struct Salary {
    inner: u64,
}

impl From<u64> for Salary {
    #[inline]
    fn from(input: u64) -> Self {
        Salary { inner: input }
    }
}

impl fmt::Debug for Salary {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.inner)
    }
}

impl fmt::Display for Salary {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}.{:02}", self.inner / 100, self.inner % 100)
    }
}

impl Add for Salary {
    type Output = Salary;

    #[inline]
    fn add(self, other: Salary) -> Salary {
        Salary::from(self.inner + other.inner)
    }
}

impl Div<u64> for Salary {
    type Output = Salary;

    #[inline]
    fn div(self, other: u64) -> Salary {
        let mut res = self.inner / other;
        if self.inner % other > other / 2 {
            res += 1;
        }
        Salary::from(res)
    }
}

impl AddAssign for Salary {
    #[inline]
    fn add_assign(&mut self, other: Salary) {
        self.inner += other.inner;
    }
}
