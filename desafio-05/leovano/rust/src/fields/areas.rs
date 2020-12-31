use super::{AreaCode, Text};
use fnv::FnvBuildHasher;
use std::ops::Index;

// use std::collections::HashMap;
use hashbrown::HashMap;

type Map<K, V, H> = HashMap<K, V, H>;
type BuildHasher = FnvBuildHasher;

#[derive(Debug, Default)]
pub struct Areas<'a> {
    inner: Map<AreaCode, Text<'a>, BuildHasher>,
}

impl<'a> Areas<'a> {
    pub fn insert(&mut self, codigo: [u8; 2], nome: Text<'a>) {
        self.inner.insert(AreaCode::from(codigo), nome);
    }
}

impl<'a, 'b> Index<&'b AreaCode> for Areas<'a> {
    type Output = Text<'a>;

    fn index(&self, idx: &'b AreaCode) -> &Text<'a> {
        &self.inner[idx]
    }
}
