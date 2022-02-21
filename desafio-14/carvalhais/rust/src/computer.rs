// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use super::prelude::*;

/// Takes a [`Token`] vector and computes the corresponding mathematical
/// expression.
///
/// This function expects that it's argument is already parsed, and reordered
/// by the shunting yard algorithm in a RPN notation (Reverse Polish Notation).
/// All this funcion does is consume the input vector, push values to a stack,
/// and consume them in reverse order for each operation, pushing the result
/// back to the stack to be consumed by the next operation.
///
/// Any other token that is not a value or a operation is considered an error;
/// a stack underflow, or a stack with a value count different than one after
/// all the operations have taken place are also considered a syntax error
/// (because it means the expression was malformed, not all errors are caught by
/// the scanning and shunting algorithms).
///
/// The algorithm also detects division by zero errors.
///
pub fn compute(tokens: Vec<Token>) -> Result<i64, ExprError> {
    let mut stack: Vec<i64> = Vec::new();
    for tk in tokens {
        let op = match tk {
            Token::Value(value) => {
                stack.push(value);
                continue;
            }
            Token::Oper(oper) => oper,
            // if the token vector contains other kinds of tokens, then it is
            // an unknown error, since they should have been stripped out by
            // the shunting algorithm
            _ => return Err(ExprError::UnexpectedToken),
        };
        // if there aren't enough values on the stack, then the expression is
        // malformed, and this is considered a syntax error
        let rhs = stack.pop().ok_or(ExprError::Syntax)?;
        let lhs = stack.pop().ok_or(ExprError::Syntax)?;
        match op {
            Procedure::Add => stack.push(lhs.wrapping_add(rhs)),
            Procedure::Sub => stack.push(lhs.wrapping_sub(rhs)),
            Procedure::Mul => stack.push(lhs.wrapping_mul(rhs)),
            Procedure::Div => {
                if rhs == 0 {
                    return Err(ExprError::DivByZero);
                }
                stack.push(lhs.wrapping_div(rhs))
            }
            Procedure::Pow => stack.push(lhs.wrapping_pow(rhs as u32)),
        }
    }
    // at the end of the computation, we should have only the result left on the
    // stack, if not it means we have a malformed mathematical expression
    if stack.len() != 1 {
        return Err(ExprError::Syntax);
    }
    Ok(stack.pop().unwrap())
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn compute_valid_expression1() {
        let expr = "1 + 2 * (3 + 4)";
        let tokens = scan(expr).unwrap();
        let tokens = shunt(tokens).unwrap();
        let result = compute(tokens).unwrap();
        assert_eq!(15, result);
    }

    #[test]
    fn compute_valid_expression2() {
        let expr = "2 ^ 1 * 3";
        let tokens = scan(expr).unwrap();
        let tokens = shunt(tokens).unwrap();
        let result = compute(tokens).unwrap();
        assert_eq!(6, result);
    }

    #[test]
    fn compute_valid_expression3() {
        let expr = "2 ^ (1 * 3)";
        let tokens = scan(expr).unwrap();
        let tokens = shunt(tokens).unwrap();
        let result = compute(tokens).unwrap();
        assert_eq!(8, result);
    }

    #[test]
    fn compute_invalid_expression1() {
        let expr = "2 (1 * 3)";
        let tokens = scan(expr).unwrap();
        let tokens = shunt(tokens).unwrap();
        let result = compute(tokens);
        assert_eq!(result, Err(ExprError::Syntax));
    }

    #[test]
    fn compute_invalid_expression2() {
        let expr = "2 1";
        let tokens = scan(expr).unwrap();
        let tokens = shunt(tokens).unwrap();
        let result = compute(tokens);
        assert_eq!(result, Err(ExprError::Syntax));
    }

    #[test]
    fn compute_div_by_zero() {
        let expr = "1 / 0";
        let tokens = scan(expr).unwrap();
        let tokens = shunt(tokens).unwrap();
        let result = compute(tokens);
        assert_eq!(result, Err(ExprError::DivByZero));
    }

    #[test]
    fn compute_unexpected_token() {
        let tokens = vec![
            Token::Paren(Direction::Left),
            Token::Paren(Direction::Right),
        ];
        let result = compute(tokens);
        assert_eq!(result, Err(ExprError::UnexpectedToken));
    }
}
