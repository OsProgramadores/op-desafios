use serde::de::{self, Deserialize, Deserializer, Visitor};
use std::fmt;

#[derive(Hash, PartialEq, Default, Clone)]
pub struct AreaCode {
    inner: [u8; 2],
}

impl fmt::Debug for AreaCode {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}{}", self.inner[0] as char, self.inner[1] as char)
    }
}

impl Eq for AreaCode {}

impl From<[u8; 2]> for AreaCode {
    #[inline]
    fn from(input: [u8; 2]) -> Self {
        AreaCode { inner: input }
    }
}

impl<'de> Deserialize<'de> for AreaCode {
    fn deserialize<D>(deserializer: D) -> Result<AreaCode, D::Error>
    where
        D: Deserializer<'de>,
    {
        struct AreaCodeVisitor;

        impl<'de> Visitor<'de> for AreaCodeVisitor {
            type Value = AreaCode;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("two ASCII characters")
            }

            fn visit_str<E>(self, value: &str) -> Result<AreaCode, E>
            where
                E: de::Error,
            {
                if value.len() != 2 {
                    return Err(E::custom("Invalid size"));
                }

                let mut chars = [0u8; 2];
                chars.clone_from_slice(value.as_bytes());

                Ok(AreaCode::from(chars))
            }
        }

        deserializer.deserialize_str(AreaCodeVisitor)
    }
}
