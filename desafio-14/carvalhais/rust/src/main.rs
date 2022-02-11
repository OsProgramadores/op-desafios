use parser::prelude::*;

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
            Ok(_) => res_parsed.unwrap(),
            Err(e) => {
                println!("{}", e);
                continue;
            }
        };
        let res_shunted = shunt(parsed);
        let shunted = match res_shunted {
            Ok(_) => res_shunted.unwrap(),
            Err(e) => {
                println!("{}", e);
                continue;
            }
        };
        let res_result = compute(shunted);
        match res_result {
            Ok(res) => println!("{}", res),
            Err(e) => println!("{}", e),
        }
    }
}
