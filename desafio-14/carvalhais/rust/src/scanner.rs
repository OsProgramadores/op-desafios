use super::prelude::*;

/// Tokenizes the input string into a vector of [`Token`]s.
///
/// Any integer values are parsed and a conversion to an i32 is tried. If this
/// conversion fails, it is considered a syntax error. Stray characters (that
/// is, one that is not either a number, a parenthesis - left or right - or an
/// operation - '+', '-', '/', '*' and '^') are also considered a syntax error.
///
/// No attempt is made to validate any other aspect of the expression, this is
/// delegated to the [`shunt`] and [`compute`] functions.
///
/// # Example
/// ```
/// let tokens = scan("1 * (2 + 3)").unwrap();
/// ```
pub fn scan(expression: &str) -> Result<Vec<Token>, &'static str> {
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
                match i64::from_str_radix(&sequence, 10) {
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
        match i64::from_str_radix(&sequence, 10) {
            Ok(num) => tokens.push(Token::Value(num)),
            Err(_) => return Err("ERR SYNTAX"),
        }
    }
    Ok(tokens)
}
