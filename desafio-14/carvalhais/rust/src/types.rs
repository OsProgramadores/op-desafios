// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

/// A direction (left or right) indicator for parentheses and associativity.
#[derive(Debug, PartialEq)]
pub enum Direction {
    Left,
    Right,
}

/// Mathematical operations known to the algorithm.
#[derive(Debug)]
pub enum Procedure {
    Add,
    Sub,
    Mul,
    Div,
    Pow,
}

impl Procedure {
    /// Returns an owned [`ProcAttr`] that contains the correct values for the
    /// concrete variant of the instance.
    pub fn attr(&self) -> ProcAttr {
        match *self {
            Procedure::Add => ProcAttr {
                precedence: 10,
                associativity: Direction::Left,
            },
            Procedure::Sub => ProcAttr {
                precedence: 10,
                associativity: Direction::Left,
            },
            Procedure::Mul => ProcAttr {
                precedence: 20,
                associativity: Direction::Left,
            },
            Procedure::Div => ProcAttr {
                precedence: 20,
                associativity: Direction::Left,
            },
            Procedure::Pow => ProcAttr {
                precedence: 30,
                associativity: Direction::Right,
            },
        }
    }
}

/// Attributes for a given mathematical operation, used for the shunting yard
/// algorithm.
pub struct ProcAttr {
    /// Operation precedence, higher value indicate a higher precedence.
    pub precedence: u8,
    /// Kind of associativity (left ou right) of the given operation.
    pub associativity: Direction,
}

/// Represents a valid token in a mathematical expression.
///
/// This could be either a numerical value, a known mathematical operation or
/// a parentheses. This abstracts the expression from it's string representation
/// to one more apropriate for algorithmic computations.
#[derive(Debug)]
pub enum Token {
    Value(i64),
    Oper(Procedure),
    Paren(Direction),
}

impl Token {
    /// Unwraps the value out of a Token::Value variant.
    pub fn unwrap_value(&self) -> i64 {
        match self {
            Token::Value(v) => *v,
            _ => panic!("expected Token::Value variant"),
        }
    }
    /// Unwraps the value out of a Token::Oper variant.
    pub fn unwrap_oper(&self) -> &Procedure {
        match self {
            Token::Oper(s) => s,
            _ => panic!("expected Token::Oper variant"),
        }
    }
    /// Unwraps the value out of a Token::Paren variant.
    pub fn unwrap_paren(&self) -> &Direction {
        match self {
            Token::Paren(d) => d,
            _ => panic!("expected Token::Paren variant"),
        }
    }
}
