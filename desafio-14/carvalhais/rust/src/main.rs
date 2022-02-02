
#[derive(Debug, PartialEq)]
enum Direction {
    Left,
    Right
}

struct ProcAttr {
    precedence: u8,
    associativity: Direction,
}

#[derive(Debug)]
enum Procedure {
    Add,
    Sub,
    Mul,
    Div,
    Pow,
}

impl Procedure {
    fn attr(&self) -> ProcAttr {
        match *self {
            Procedure::Add => ProcAttr{ 
                precedence: 10,
                associativity: Direction::Left,
            },
            Procedure::Sub => ProcAttr{
                precedence: 10,
                associativity: Direction::Left,
            },
            Procedure::Mul => ProcAttr{
                precedence: 20,
                associativity: Direction::Left,
            },
            Procedure::Div => ProcAttr{
                precedence: 20,
                associativity: Direction::Left,
            },
            Procedure::Pow => ProcAttr{
                precedence: 30,
                associativity: Direction::Right,
            },
        }
    }
}

#[derive(Debug)]
enum Token {
    Value(u64),
    Oper(Procedure),
    Paren(Direction),
}

impl Token {
    fn unwrap_value(&self) -> u64 {
        match self {
            Token::Value(v) => *v,
            _ => panic!("expected Token::Value variant")
        }
    }

    fn unwrap_oper(&self) -> &Procedure {
        match self {
            Token::Oper(s) => s,
            _ => panic!("expected Token::Oper variant")
        }
    }

    fn unwrap_paren(&self) -> &Direction {
        match self {
            Token::Paren(d) => d,
            _ => panic!("expected Token::Paren variant")
        }
    }
}

fn scan(expression: &str) -> Result<Vec<Token>, &'static str> {
    let mut tokens: Vec<Token> = Vec::new();
    let mut sequence = String::new();
    let mut seq_flag: bool = false;

    for ch in expression.chars() {
        // test if we are mid sequence; take into account that only operands can
        // be a sequence in mathematical expressions
        if seq_flag {
            // char is a digit, push it to the operand sequence and iterate
            if ch.is_ascii_digit() {
                sequence.push(ch);
                continue;
            }
            // char is not a digit, the operand sequence is over; finish the 
            // sequence and fall through the rest of the loop to process 'ch'
            else {
                seq_flag = false;
                // try to convert the sequence into a number and reset sequence
                // state; if the conversion fails, we've got a syntax error
                match u64::from_str_radix(&sequence, 10) {
                    Ok(num) => {
                        tokens.push(Token::Value(num));
                        sequence.clear();
                    }
                    // if the conversion fails, we have a badly formatted number
                    Err(_) => {
                        return Err("ERR SYNTAX");
                    }
                }
            }
            
        }
        // ignore whitespace
        if ch.is_ascii_whitespace() {
            continue;
        }
        // match all known characters
        match ch {
            // a digit means the beginning of a new sequence
            '0'..='9' => {
                seq_flag = true;
                sequence.push(ch);
            }
            // mathematical operations
            '+' => tokens.push(Token::Oper(Procedure::Add)),
            '-' => tokens.push(Token::Oper(Procedure::Sub)),
            '*' => tokens.push(Token::Oper(Procedure::Mul)),
            '/' => tokens.push(Token::Oper(Procedure::Div)),
            '^' => tokens.push(Token::Oper(Procedure::Pow)),
            // parentheses
            '(' => tokens.push(Token::Paren(Direction::Left)),
            ')' => tokens.push(Token::Paren(Direction::Right)),
            // any other char means we have a bad expression
            _ => return Err("ERR SYNTAX"),
        }
    }
    // when the expresion finishes with a number, this number characters are 
    // left on the sequence variable without being pushed to the token vector
    // so we check this now and push the value; so we push this value if the
    // sequence is not empty
    if !sequence.is_empty() {
        match u64::from_str_radix(&sequence, 10) {
            Ok(num) => tokens.push(Token::Value(num)),
            Err(_) => return Err("ERR SYNTAX"),
        }
    }
    Ok(tokens)
}

fn shunt(tokens: Vec<Token>) -> Result<Vec<Token>, &'static str> {
    let mut output: Vec<Token> = Vec::new();
    let mut stack: Vec<Token> = Vec::new();

    for token in tokens {
        // a) if the incoming symbol is an operand, print it
        if let Token::Value(_) = token {
            output.push(token);
            continue;
        }
        // b) if the incoming symbol is a left parenthesis, push it on the stack
        if let Token::Paren(Direction::Left) = token {
            stack.push(token);
            continue;
        }
        // c) if the incoming symbol is a right parenthesis: discard the right
        // parenthesis, pop and print the stack symbols until you see a left
        // parenthesis; pop the left parenthesis and discard it
        if let Token::Paren(Direction::Right) = token {
            loop {
                let tos = stack.pop();
                // if we reach the end of the stack without a matching left 
                // parenthesis, that's a syntax error
                if tos.is_none() {
                    return Err("ERR SYNTAX");
                }
                // tos isn't a None, unwrap it
                let tos = tos.unwrap();
                // pop and print the stack symbols until you see a left
                // parenthesis
                if let Token::Oper(_) = tos {
                    output.push(tos);
                    continue;
                }
                // pop the left parenthesis and discard it
                if let Token::Paren(Direction::Left) = tos {
                    break;
                }
                // anything else is a syntax error, so if we reach the following
                // statement, we should return an error
                return Err("ERR SYNTAX");
            }
            continue;
        // handle mathematical operations precedence
        }
        if let Token::Oper(_) = token {
            // d) if the incoming symbol is an operator and the stack is empty 
            // or contains a left parenthesis on top, push the incoming operator 
            // onto the stack
            let opt_tos = stack.pop();
            // the stack is empty
            if opt_tos.is_none() {
                stack.push(token);
                continue;
            }
            // opt_tos isn't None, unwrap it
            let mut tos = opt_tos.unwrap();
            // contains a left parenthesis on top
            if let Token::Paren(Direction::Left) = tos {
                stack.push(tos);
                stack.push(token);
                continue;
            }
            // e) if the incoming symbol is an operator and has either higher
            // precedence than the operator on the top of the stack, or has the
            // same precedence as the operator on the top of the stack and is
            // right associative -- push it on the stack
            let token_attr = token.unwrap_oper().attr();
            let mut tos_attr = tos.unwrap_oper().attr();

            let higher = token_attr.precedence > tos_attr.precedence;
            let equal = token_attr.precedence == tos_attr.precedence;
            let right = token_attr.associativity == Direction::Right;

            if higher || (equal && right) {
                stack.push(tos);
                stack.push(token);
                continue;
            }

            // f) if the incoming symbol is an operator and has either lower
            // precedence than the operator on the top of the stack, or has
            // the same precedence as the operator on the top of the stack and
            // is left associative -- continue to pop the stack until this is
            // not true; then, push the incoming operator
            let mut lower = token_attr.precedence < tos_attr.precedence;
            let mut equal = token_attr.precedence == tos_attr.precedence;
            let mut left = token_attr.associativity == Direction::Left;
            loop {
                if lower || (equal && left) {
                    output.push(tos);
                }
                else {
                    stack.push(tos);
                    stack.push(token);
                    break;
                }
                if stack.len() >= 1 {
                    // if theere is an operator on top of the stack, reevaluate
                    // the loop; if the top of stack is a left paren, it means
                    // we reached the end of the current 'stream' of oprations,
                    // so just puch things back in the stack and keep going;
                    // anything else is a syntax error
                    tos = stack.pop().unwrap();
                    match tos {
                        Token::Oper(_) => {
                            tos_attr = tos.unwrap_oper().attr();
                            lower = token_attr.precedence > tos_attr.precedence;
                            equal = token_attr.precedence == tos_attr.precedence;
                            left = token_attr.associativity == Direction::Right;
                        }
                        Token::Paren(Direction::Left) => {
                            stack.push(tos);
                            stack.push(token);
                            break;
                        }
                        _ => return Err("ERR SYNTAX"),
                    }
                }
                else {
                    stack.push(token);
                    break;
                }
            }
        }
    }
    // at the end of the expression, pop and print all operators on the stack;
    // (no parentheses should remain)
    while let Some(token) = stack.pop() {
        match token {
            Token::Oper(_) => output.push(token),
            _ => return Err("ERR SYNTAX"),
        }
    }
    Ok(output)
}

fn main() {
    let expressions = [
        "1 ^ (2 + 3)",
        "1 ^ (2 + 3 ^ 4)",
        "1 * (2 + 3) ^ 4",
        "1 * 2 * 3 + 4",
        "((1 * 2) + 3) * 4 + 5",
        "((1 + 2) ^ 3 * 4) + 5",
        "((1 + 2) ^ 3 * 4) * 5",
        "(((1 + 2) ^ 3 * 4) ^ 5)",
        "1 + 3",
        "2 - 3 * 2",
        "2 ^ 3 / 4",
        "0 * 5 * (4 + 1)",
        "5 + 5 / 0",
        "5 + + 1",
        "5 + ( 465 + 1",
    ];

    for expr in expressions {
        let res_parsed = scan(expr);
        let parsed = match res_parsed {
            Ok(_) => {
                println!("parseable");
                res_parsed.unwrap()
            },
            Err(e) => {
                println!("{}", e);
                continue;
            }
        };
        let res_shunted = shunt(parsed);
        match res_shunted {
            Ok(_) => {
                println!("shuntable");
            }
            Err(e) => {
                println!("{}", e);
                continue;
            }
        }
        println!("");
    }
}
