// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use super::prelude::*;

/// Tries to convert the number in `&str` into a `i64`
///
fn helper_num_conversion(s: &str) -> Result<i64, ExprError> {
    // try to convert the sequence into a number
    match i64::from_str_radix(s, 10) {
        Ok(num) => Ok(num),
        // if the conversion fails, we have a badly formatted number
        Err(_) => Err(ExprError::NumConversion),
    }
}

/// Tokenizes the input string into a vector of [`Token`].
///
/// Any integer values are parsed and a conversion to an i64 is tried. If this
/// conversion fails, it is considered an error. Stray characters (that is, one
/// that is not either a number, a parenthesis - left or right - or an
/// operation -- '+', '-', '/', '*' and '^') are also considered an error.
///
/// No attempt is made to validate any other aspect of the expression, this is
/// delegated to the [`shunt`] and [`compute`] functions.
///
pub fn scan(expression: &str) -> Result<Vec<Token>, ExprError> {
    let mut tokens: Vec<Token> = Vec::new();
    let mut operand = String::new();
    let mut chars = expression.chars().fuse();
    'expr: while let Some(mut ch) = chars.next() {
        // if the char is a digit, we have an operand, decode the whole operand
        // before proceeding
        if ch.is_ascii_digit() {
            loop {
                operand.push(ch);
                ch = match chars.next() {
                    Some(c) => c,
                    None => continue 'expr,
                };
                if !ch.is_ascii_digit() {
                    break;
                }
            }
            // convert the number just consumed and push it to the stack
            let value = helper_num_conversion(&operand)?;
            tokens.push(Token::Value(value));
            // clear the operand string, so it can handle the next operand
            operand.clear();
        }
        // match all other characters
        match ch {
            // ignore whitespace
            ws if ws.is_ascii_whitespace() => continue,
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
            _ => return Err(ExprError::StrayChar),
        }
    }
    // if the inner loop hits the end of the expression while processing a
    // number, it 'continues' the outer loop, but because we have a fused
    // iterator, it is guaranteed to exit the while loop; the last operand is
    // still unconverted on the 'operand' string, however; so we convert it and
    // push it to the stack
    if !operand.is_empty() {
        let value = helper_num_conversion(&operand)?;
        tokens.push(Token::Value(value));
    }
    Ok(tokens)
}
