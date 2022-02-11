#[derive(Debug, PartialEq)]
pub enum Direction {
    Left,
    Right,
}

pub struct ProcAttr {
    pub precedence: u8,
    pub associativity: Direction,
}

#[derive(Debug)]
pub enum Procedure {
    Add,
    Sub,
    Mul,
    Div,
    Pow,
}

impl Procedure {
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

#[derive(Debug)]
pub enum Token {
    Value(i64),
    Oper(Procedure),
    Paren(Direction),
}

impl Token {
    pub fn unwrap_value(&self) -> i64 {
        match self {
            Token::Value(v) => *v,
            _ => panic!("expected Token::Value variant"),
        }
    }

    pub fn unwrap_oper(&self) -> &Procedure {
        match self {
            Token::Oper(s) => s,
            _ => panic!("expected Token::Oper variant"),
        }
    }

    pub fn unwrap_paren(&self) -> &Direction {
        match self {
            Token::Paren(d) => d,
            _ => panic!("expected Token::Paren variant"),
        }
    }
}
