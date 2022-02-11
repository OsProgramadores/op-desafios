// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use super::prelude::*;

pub fn compute(tokens: Vec<Token>) -> Result<i64, &'static str> {
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
            _ => return Err("ERR UNKNOWN"),
        };
        // if there aren't enough values on the stack, then the expression is
        // malformed, and this is considered a syntax error
        let rhs = stack.pop().ok_or("ERR SYNTAX")?;
        let lhs = stack.pop().ok_or("ERR SYNTAX")?;
        match op {
            Procedure::Add => stack.push(lhs.wrapping_add(rhs)),
            Procedure::Sub => stack.push(lhs.wrapping_sub(rhs)),
            Procedure::Mul => stack.push(lhs.wrapping_mul(rhs)),
            Procedure::Div => {
                if rhs == 0 {
                    return Err("ERR DIVBYZERO");
                }
                stack.push(lhs.wrapping_div(rhs))
            }
            Procedure::Pow => stack.push(lhs.wrapping_pow(rhs as u32)),
        }
    }
    // at the end of the computation, we should have only the result left on the
    // stack, if not it means we have a malformed mathematical expression
    if stack.len() != 1 {
        return Err("ERR SYNTAX");
    }
    Ok(stack.pop().unwrap())
}
