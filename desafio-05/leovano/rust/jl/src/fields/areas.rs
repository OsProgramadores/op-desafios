use super::AreaCode;
use std::ops::Index;
use utils::FnvBuildHasher;

use std::collections::hash_map::HashMap;

type Map<K, V, H> = HashMap<K, V, H>;
type BuildHasher = FnvBuildHasher;

#[derive(Debug, Default)]
pub struct Areas<'a> {
    inner: Map<AreaCode, &'a [u8], BuildHasher>,
}

impl<'a> Areas<'a> {
    #[inline]
    pub fn insert(&mut self, codigo: [u8; 2], nome: &'a [u8]) {
        self.inner.insert(AreaCode::from(codigo), nome);
    }
}

impl<'a, 'b> Index<&'b AreaCode> for Areas<'a> {
    type Output = str;

    #[inline]
    fn index(&self, idx: &'b AreaCode) -> &str {
        ::std::str::from_utf8(&self.inner[idx]).expect("Utf8Fail")
    }
}
