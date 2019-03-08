use std::num::ParseIntError;

#[derive(Debug)]
pub enum ConvError {
    InvalidCharacter,
    InvalidCharacterForRadix,
    InvalidInput,
    InvalidRadix,
    Parsing(ParseIntError),
    TooBigNumber,
}

impl From<ParseIntError> for ConvError {
    fn from(input: ParseIntError) -> Self {
        ConvError::Parsing(input)
    }
}

