use serde::de::{self, Deserialize, Deserializer, Visitor};
use std::ops::{Add, AddAssign};
use std::{f64, fmt};

#[derive(Clone, Default, PartialEq, PartialOrd)]
pub struct Salary {
    inner: f32,
}

impl fmt::Debug for Salary {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.inner)
    }
}

impl fmt::Display for Salary {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:.2}", self.inner)
    }
}

impl<'a> Add for &'a Salary {
    type Output = Sum;

    #[inline]
    fn add(self, other: &'a Salary) -> Sum {
        Sum::from(f64::from(self.inner) + f64::from(other.inner))
    }
}

impl From<f64> for Salary {
    #[inline]
    fn from(input: f64) -> Self {
        Salary {
            inner: input as f32,
        }
    }
}

impl<'de> Deserialize<'de> for Salary {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        struct SalaryVisitor;

        impl<'de> Visitor<'de> for SalaryVisitor {
            type Value = Salary;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("a float")
            }

            fn visit_f64<E>(self, value: f64) -> Result<Salary, E>
            where
                E: de::Error,
            {
                Ok(Salary::from(value))
            }
        }

        deserializer.deserialize_f64(SalaryVisitor)
    }
}

pub struct Sum {
    inner: f64,
}

impl Sum {
    #[inline]
    pub fn average(&self, employees: usize) -> Sum {
        Sum::from(self.inner / employees as f64)
    }
}

impl fmt::Debug for Sum {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.inner)
    }
}

impl fmt::Display for Sum {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:.2}", self.inner)
    }
}

impl<'a> AddAssign<&'a Salary> for Sum {
    #[inline]
    fn add_assign(&mut self, other: &'a Salary) {
        self.inner += f64::from(other.inner);
    }
}

impl From<f64> for Sum {
    #[inline]
    fn from(input: f64) -> Self {
        Sum { inner: input }
    }
}

impl<'a> From<&'a Salary> for Sum {
    #[inline]
    fn from(input: &'a Salary) -> Self {
        Sum {
            inner: f64::from(input.inner),
        }
    }
}
