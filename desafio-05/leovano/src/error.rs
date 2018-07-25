use serde_json;
use std::io;

#[derive(Debug)]
pub enum Error {
    IO(io::Error),
    SerdeJson(serde_json::Error),
}

impl From<io::Error> for Error {
    fn from(input: io::Error) -> Self {
        Error::IO(input)
    }
}

impl From<serde_json::Error> for Error {
    fn from(input: serde_json::Error) -> Self {
        Error::SerdeJson(input)
    }
}
