// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use super::prelude::*;

/// Implements Dijkstra's shuting-yard algorithm over the [`Token`] vector.
///
/// The shunting-yard algorithm takes a token vector representing a regular
/// mathematical expression and rearrange it into a postfix notation (sometimes
/// also called Reverse Polish Notation) which is directly computable by a
/// computer program. The rearranged expression is also given in termos of a
///  [`Token`]  vector.
///
/// This implementation is based on the algorithm description summarized in
/// http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/.
///

pub fn shunt(tokens: Vec<Token>) -> Result<Vec<Token>, &'static str> {
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
                } else {
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
                } else {
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
