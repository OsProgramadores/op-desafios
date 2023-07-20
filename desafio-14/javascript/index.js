const fs = require("fs");

function get(file) {
    try {
        const data = fs.readFileSync(file, "utf8").split("\n");
        const expressions = [];

        for (let expression of data) {
            if (expression !== "") {
                expression = expression.split(" ").join("");
                expressions.push(expression);
            }
        }

        return expressions;
    } catch (err) {
        console.error(err, "Read Failed");
        return err;
    }
}

function isValidExpression(expression) {
    const haveParentheses = expression.includes("(");

    if (haveParentheses) {
        expression = expression.split("");

        const amountOpeningParenthesis = expression.reduce(
            (count, char) => (char === "(" ? count + 1 : count),
            0
        );

        const amountClosingParenthesis = expression.reduce(
            (count, char) => (char === ")" ? count + 1 : count),
            0
        );

        if (amountOpeningParenthesis !== amountClosingParenthesis) {
            return false;
        }
    }

    for (let i = 0; i <= expression.length; i++) {
        const operators = ["+", "-", "*", "/", "^"];

        const currentChar = expression[i];
        const nextChar = expression[i + 1];

        if (operators.includes(currentChar) && operators.includes(nextChar)) {
            return false;
        }
    }

    return true;
}

function infixToPostfix(expression) {
    const precedence = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2
    };

    const result = [];
    const stack = [];

    for (const token of expression) {
        const isNumber = !isNaN(token);

        if (isNumber) {
            result.push(token);
        } else if (token === "(") {
            stack.push(token);
        } else if (token === ")") {
            while (stack[stack.length - 1] !== "(") {
                const lastOperator = stack.pop();

                result.push(lastOperator);
            }

            stack.pop();
        } else {
            while (stack[stack.length - 1] &&
        precedence[token] <= precedence[stack[stack.length - 1]]
            ) {
                const lastOperator = stack.pop();

                result.push(lastOperator);
            }
            stack.push(token);
        }
    }

    while (stack.length > 0) {
        result.push(stack.pop());
    }

    return result;
}

function solvePostfixExpression(expression) {
    const stack = [];

    for (const token of expression) {
        const isNumber = !isNaN(token);

        if (isNumber) {
            stack.push(parseInt(token));
        } else {
            const operand1 = stack.pop();
            const operand0 = stack.pop();

            switch (token) {
                case "+":
                    stack.push(operand0 + operand1);
                    break;
                case "-":
                    stack.push(operand0 - operand1);
                    break;
                case "*":
                    stack.push(operand0 * operand1);
                    break;
                case "/":
                    if (operand1 === 0) {
                        return "ERR DIVBYZERO";
                    }
                    stack.push(operand0 / operand1);
                    break;
                case "^":
                    stack.push(operand0 ** operand1);
                    break;
            }
        }
    }
    const result = stack.pop();

    return result;
}

function main() {
    const file = process.argv[2];
    const data = get(file);

    for (let expression of data) {
        const isValid = isValidExpression(expression);

        if (!isValid) {
            console.log("ERR SYNTAX");
            continue;
        }

        expression = expression.split(/([()+\-/*^])/).filter(Boolean);

        const postfix = infixToPostfix(expression);

        const result = solvePostfixExpression(postfix);

        console.log(result);
    }
}

main();