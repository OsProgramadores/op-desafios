use std::mem::{self, replace, swap};
use std::ops::Deref;
use std::sync::Arc;

pub enum Aoc<T> {
    Owned(T),
    Shared(Arc<T>),
}

impl<T> Aoc<T> {
    pub fn new(value: T) -> Self {
        Aoc::Owned(value)
    }

    pub fn share(this: &mut Aoc<T>) -> Arc<T> {
        match this {
            Aoc::Owned(value) => {
                let void = unsafe { mem::uninitialized() };
                let curr = replace(value, void);
                let curr = Arc::new(curr);
                let clone = Arc::clone(&curr);
                let curr = Aoc::Shared(curr);
                let void = replace(this, curr);
                mem::forget(void);
                clone
            }
            Aoc::Shared(value) => Arc::clone(value),
        }
    }
}

impl<T> Deref for Aoc<T> {
    type Target = T;

    fn deref(&self) -> &T {
        match self {
            Aoc::Owned(value) => value,
            Aoc::Shared(value) => value,
        }
    }
}
