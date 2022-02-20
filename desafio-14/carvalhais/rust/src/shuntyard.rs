// numeric_expressions - a rust solution for challenge #14 from OsProgramadores
// website implementing Dijkstra's shunting yard algorithm
//
// (c) Andre Carvalhais <carvalhais@live.com>
//
// For the full copyright and license information, please view the LICENSE file
// that was distributed with this source code.

use super::prelude::*;
use core::iter::Peekable;
use std::vec::IntoIter;

/// Helper function to handle the right parenthesis case.
///
/// This function is called whenever the shunting yard algorithm finds a right
/// parenthesis. It discards the right parenthesis, and looks for the matching
/// left parenthesis, popping every tokens from the stack and pushing them to
/// the output until the matching left parenthesis is found.
///
/// If the end of the stack is reached before the matching left parenthesis is
/// found, this is considered an error. If tokens other than operations and left
/// parenthesis are found, this is also considered an error.
///
fn handle_right_paren(
    tokens: &mut Peekable<IntoIter<Token>>,
    output: &mut Vec<Token>,
    stack: &mut Vec<Token>,
) -> Result<(), ExprError> {
    // assert that the next symbol in the expression vector is a right
    // parenthesis, if it is not, something really bad must have hapenned
    // (since this function is not exposed to the public API, and only called
    // internally), so we panic; if things are just okay, pop and discard the
    // right parenthesis
    if tokens.next() != Some(Token::Paren(Direction::Right)) {
        panic!("unrecoverable state in function 'handle_right_paren'");
    }
    // pop and output the stack symbols until you see a left parenthesis
    loop {
        let tos = stack.pop();
        // if we reach the end of the stack without a matching left
        // parenthesis, that's a syntax error
        if tos.is_none() {
            return Err(ExprError::UnbalancedParen);
        }
        // tos isn't a None, unwrap it
        let tos = tos.unwrap();
        // pop and output the stack symbols until you see a left parenthesis
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
        return Err(ExprError::UnexpectedToken);
    }
    Ok(())
}

/// Helper function to handle the lower precedence or same precedence with left
/// associativity case.
///
/// This function is called whenever the incoming operation symbol  from the
/// parsed expression has either a lower precedence than the symbol on the top
/// of the stack, or has the same precedence, but it is left associative. It
/// consumes the stack, popping it's symbols and pushing them on the output
/// until this condition is no longer met. Then, the incoming symbol is pushed
/// into the stack.
///
/// Since it is considered a normal operating condition to reach the end of the
/// stack or an operator that has different precedence and / or associativity
/// characteristics than the ones needed to keep iterating, this function simply
/// returns on such situations, and returns no error.
///
fn handle_lower_left(
    tokens: &mut Peekable<IntoIter<Token>>,
    output: &mut Vec<Token>,
    stack: &mut Vec<Token>,
) -> Result<(), ExprError> {
    // we know the incoming token is an operator, because we got called
    let incoming = tokens.next().unwrap();
    let in_attr;
    if let Token::Oper(any) = &incoming {
        in_attr = any.attr();
    // something really bad happened, so we just panic
    } else {
        panic!("unrecoverable state in function 'handle_same_left'");
    }

    // iteratively consume the stack
    while let Some(tos) = stack.last() {
        // the stack only contains operators or (optionally) left parenthesis
        // (since right parenthesis are discarded as soon as they're read), but
        // we want to stop processing if we reach a left parenthesis or the
        // end of the stack
        let tos_attr;
        if let Token::Oper(any) = tos {
            tos_attr = any.attr();
        // tos is not an operator or the stack is empty, we're done
        } else {
            break;
        }
        // the incoming symbol is an operator and has either lower precedence
        // than the operator on the top of the stack, or has the same precedence
        // as the operator on the top of the stack and is left associative
        let lower = in_attr.precedence < tos_attr.precedence;
        let same = in_attr.precedence == tos_attr.precedence;
        let l_assoc = in_attr.associativity == Direction::Left;
        // continue to pop the stack until this is not true
        if lower || (same && l_assoc) {
            let symbol = stack.pop().unwrap();
            output.push(symbol);
        } else {
            break;
        }
    }
    // push the incoming operator
    stack.push(incoming);
    Ok(())
}

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
pub fn shunt(tkns: Vec<Token>) -> Result<Vec<Token>, ExprError> {
    let mut output: Vec<Token> = Vec::new();
    let mut stack: Vec<Token> = Vec::new();
    let mut tokens = tkns.into_iter().peekable();

    while let Some(peeked) = tokens.peek() {
        match peeked {
            // a) if the incoming symbol is an operand, output it
            Token::Value(_) => output.push(tokens.next().unwrap()),
            // b) if the incoming symbol is a left parenthesis, push it on the stack
            Token::Paren(Direction::Left) => stack.push(tokens.next().unwrap()),
            // c) if the incoming symbol is a right parenthesis: discard the
            // right parenthesis, pop and output the stack symbols until you see
            // a left parenthesis; pop the left parenthesis and discard it
            Token::Paren(Direction::Right) => {
                handle_right_paren(&mut tokens, &mut output, &mut stack)?
            }
            Token::Oper(_) => {
                // d) if the incoming symbol is an operator and the stack is
                // empty or contains a left parenthesis on top, push the
                // incoming operator onto the stack
                let empty = stack.len() == 0;
                let left_paren = stack.last() == Some(&Token::Paren(Direction::Left));
                if empty || left_paren {
                    stack.push(tokens.next().unwrap());
                    continue;
                }
                // e) if the incoming symbol is an operator and has either
                // higher precedence than the operator on the top of the stack,
                // or has the same precedence as the operator on the top of the
                // stack and is right associative -- push it on the stack
                let in_attr = &peeked.unwrap_oper().attr();
                let tos_attr = &stack.last().unwrap().unwrap_oper().attr();
                let higher = in_attr.precedence > tos_attr.precedence;
                let same = in_attr.precedence == tos_attr.precedence;
                let r_assoc = in_attr.associativity == Direction::Right;
                if higher || (same && r_assoc) {
                    stack.push(tokens.next().unwrap());
                    continue;
                }
                // f) if the incoming symbol is an operator and has either lower
                // precedence than the operator on the top of the stack, or has
                // the same precedence as the operator on the top of the stack
                // and is left associative -- continue to pop the stack until
                // this is not true; then, push the incoming operator
                let lower = in_attr.precedence < tos_attr.precedence;
                let l_assoc = in_attr.associativity == Direction::Left;
                if lower || (same && l_assoc) {
                    handle_lower_left(&mut tokens, &mut output, &mut stack)?;
                    continue;
                }
            }
        }
    }
    // output any remaining tokens left on the stack
    while let Some(tk) = stack.pop() {
        output.push(tk);
    }
    Ok(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn expr_from_tokens(tokens: &Vec<Token>) -> String {
        let mut expr = String::new();
        for token in tokens {
            match token {
                Token::Oper(proc) => match proc {
                    Procedure::Add => expr.push_str("+ "),
                    Procedure::Sub => expr.push_str("- "),
                    Procedure::Mul => expr.push_str("* "),
                    Procedure::Div => expr.push_str("/ "),
                    Procedure::Pow => expr.push_str("^ "),
                },
                Token::Paren(dir) => match dir {
                    Direction::Left => expr.push_str("( "),
                    Direction::Right => expr.push_str(") "),
                },
                Token::Value(num) => {
                    let num = format!("{} ", num);
                    expr.push_str(num.as_str());
                }
            }
        }
        expr.pop();
        expr
    }

    #[test]
    fn single_operation() {
        let infix = "1 + 2";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 +");
    }

    #[test]
    fn chained_left_assoc() {
        let infix = "1 * 2 * 3 * 4";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 * 3 * 4 *");
    }

    #[test]
    fn chained_right_assoc() {
        let infix = "1 ^ 2 ^ 3 ^ 4";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 3 4 ^ ^ ^");
    }

    #[test]
    fn different_precedence1() {
        let infix = "1 + 2 * 3 + 4";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 3 * + 4 +");
    }

    #[test]
    fn different_precedence2() {
        let infix = "1 + 2 + 3 * 4";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 + 3 4 * +");
    }

    #[test]
    fn different_precedence3() {
        let infix = "1 * 2 ^ 3 * 4 - 5";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 3 ^ * 4 * 5 -");
    }

    #[test]
    fn different_precedence4() {
        let infix = "1 * 2 ^ 3 - 4 * 5";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 3 ^ * 4 5 * -");
    }

    #[test]
    fn different_precedence5() {
        let infix = "1 * 2 ^ 3 ^ 4 / 5";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 3 4 ^ ^ * 5 /");
    }

    #[test]
    fn parenthesized_expression1() {
        let infix = "( 1 * 2 ) * 3 + 4";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 * 3 * 4 +");
    }

    #[test]
    fn parenthesized_expression2() {
        let infix = "( 1 * 2 ) * ( 3 + 4 )";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 * 3 4 + *");
    }

    #[test]
    fn parenthesized_expression3() {
        let infix = "( ( ( 1 + 2 ) *  3 ) + 4 ) * 5";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 + 3 * 4 + 5 *");
    }

    #[test]
    fn parenthesized_expression4() {
        let infix = "( ( ( 1 + 2 *  3 ) ^ 4 ) * 5 )";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "1 2 3 * + 4 ^ 5 *");
    }

    #[test]
    fn parenthesized_expression5() {
        let infix = "0 ^ ( 1 * ( 2 - 3 ) / 4 ) - 5 * ( 6 + 7 )";
        let tokens = shunt(scan(infix).unwrap()).unwrap();
        let rpn = expr_from_tokens(&tokens);
        assert_eq!(rpn, "0 1 2 3 - * 4 / ^ 5 6 7 + * -");
    }

    // tests that should fail
    #[test]
    #[should_panic]
    fn handle_right_paren_no_right_paren_tos() {
        let mut tokens = scan("2 1 -").unwrap().into_iter().peekable();
        let mut output: Vec<Token> = Vec::new();
        let mut stack = Vec::new();
        let _ = handle_right_paren(&mut tokens, &mut output, &mut stack);
    }

    #[test]
    fn handle_right_paren_unbalanced_paren() {
        let mut tokens = scan(") 2 1 -").unwrap().into_iter().peekable();
        let mut output: Vec<Token> = Vec::new();
        let mut stack = Vec::new();
        let result = handle_right_paren(&mut tokens, &mut output, &mut stack);
        assert_eq!(result, Err(ExprError::UnbalancedParen));
    }

    #[test]
    fn handle_right_paren_unexpected_token() {
        let mut tokens = scan(") - + * 1").unwrap().into_iter().peekable();
        let mut output: Vec<Token> = Vec::new();
        let mut stack = scan("- + * 1").unwrap();
        let result = handle_right_paren(&mut tokens, &mut output, &mut stack);
        assert_eq!(result, Err(ExprError::UnexpectedToken));
    }
}

#[test]
#[should_panic]
fn handle_lower_left_incoming_not_oper() {
    let mut tokens = scan("2 1 -").unwrap().into_iter().peekable();
    let mut output: Vec<Token> = Vec::new();
    let mut stack = Vec::new();
    let _ = handle_right_paren(&mut tokens, &mut output, &mut stack);
}
