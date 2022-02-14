// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use super::prelude::*;

/// Helper function to convert the number in `&str` into a `i64`.
///
fn handle_num_conversion(s: &str) -> Result<i64, ExprError> {
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
            let value = handle_num_conversion(&operand)?;
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
        let value = handle_num_conversion(&operand)?;
        tokens.push(Token::Value(value));
    }
    Ok(tokens)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn scan_operations() {
        let result = scan(" + - * / ^ ").unwrap();
        assert!(
            result
                == [
                    Token::Oper(Procedure::Add),
                    Token::Oper(Procedure::Sub),
                    Token::Oper(Procedure::Mul),
                    Token::Oper(Procedure::Div),
                    Token::Oper(Procedure::Pow),
                ]
        );
    }

    #[test]
    fn scan_parens() {
        let result = scan(" ( ) ").unwrap();
        assert!(
            result
                == [
                    Token::Paren(Direction::Left),
                    Token::Paren(Direction::Right),
                ]
        );
    }

    #[test]
    fn scan_value() {
        let result = scan(" 93 ").unwrap();
        assert!(result == [Token::Value(93)]);
    }

    #[test]
    fn scan_multiple_values() {
        let result = scan(" 93 2006 02042019 ").unwrap();
        assert!(result == [Token::Value(93), Token::Value(2006), Token::Value(2042019),]);
    }

    #[test]
    fn consume_whitespace() {
        let result = scan(" \t  \r\n  \n  ").unwrap();
        assert!(result == []);
    }

    #[test]
    fn math_expr1() {
        let result = scan("(1 + 2) * 3").unwrap();
        assert!(
            result
                == [
                    Token::Paren(Direction::Left),
                    Token::Value(1),
                    Token::Oper(Procedure::Add),
                    Token::Value(2),
                    Token::Paren(Direction::Right),
                    Token::Oper(Procedure::Mul),
                    Token::Value(3),
                ]
        );
    }

    #[test]
    fn math_expr2() {
        let result = scan("1^2/(3-4)").unwrap();
        assert!(
            result
                == [
                    Token::Value(1),
                    Token::Oper(Procedure::Pow),
                    Token::Value(2),
                    Token::Oper(Procedure::Div),
                    Token::Paren(Direction::Left),
                    Token::Value(3),
                    Token::Oper(Procedure::Sub),
                    Token::Value(4),
                    Token::Paren(Direction::Right),
                ]
        );
    }

    #[test]
    fn stray_char1() {
        let result = scan("?");
        assert!(result == Err(ExprError::StrayChar));
    }

    #[test]
    fn stray_char2() {
        let result = scan("$");
        assert!(result == Err(ExprError::StrayChar));
    }

    #[test]
    fn stray_char3() {
        let result = scan("e");
        assert!(result == Err(ExprError::StrayChar));
    }

    #[test]
    fn conversion1() {
        let result = handle_num_conversion("4321");
        assert!(result == Ok(4321));
    }

    #[test]
    fn conversion2() {
        let result = handle_num_conversion("987a8");
        assert!(result == Err(ExprError::NumConversion));
    }
}
