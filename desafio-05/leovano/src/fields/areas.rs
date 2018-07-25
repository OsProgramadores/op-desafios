use super::AreaCode;
use indexmap::IndexMap;
use serde::de::{Deserialize, Deserializer, SeqAccess, Visitor};
use std::fmt;
use std::ops::Index;

use fnv::FnvBuildHasher;

#[derive(Debug, Deserialize, Default)]
struct Area {
    codigo: AreaCode,
    nome: String,
}

#[derive(Debug, Default)]
pub struct Areas {
    inner: IndexMap<AreaCode, String, FnvBuildHasher>,
}

impl Areas {
    #[inline]
    fn insert(&mut self, area: Area) {
        self.inner.insert(area.codigo, area.nome);
    }
}

impl<'a> Index<&'a AreaCode> for Areas {
    type Output = String;

    #[inline]
    fn index(&self, idx: &'a AreaCode) -> &String {
        &self.inner[idx]
    }
}

impl<'de> Deserialize<'de> for Areas {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        struct AreasVisitor;

        impl<'de> Visitor<'de> for AreasVisitor {
            type Value = Areas;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("an array of maps")
            }

            fn visit_seq<V>(self, mut seq: V) -> Result<Areas, V::Error>
            where
                V: SeqAccess<'de>,
            {
                let mut areas = Areas::default();

                while let Some(entry) = seq.next_element()? {
                    areas.insert(entry)
                }

                Ok(areas)
            }
        }

        deserializer.deserialize_seq(AreasVisitor)
    }
}
