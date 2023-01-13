const fs = require("fs");

function readNumericalExpressions(path) {
    fs.readFile(path, "utf-8", function (error, data) {
        if (error) {
            console.log("erro de leitura: " + error.message);
        } else {
            let numericalExpressions;
            if ((/(\r)/.test(data))) {
                numericalExpressions = data.split("\r\n");
            } else {
                numericalExpressions = data.split("\n");
            }
            numericalExpressions = numericalExpressions.slice(0, -1);
            for (let index = 0; index < numericalExpressions.length; index++) {
                const element = numericalExpressions[index];
                const expression = element.split(" ").join("").split(/(\d|\(|\))/);
                expression.shift();
                expression.pop();
                expression.forEach(function (item, i) { if (item === "") expression[i] = "c"; });
                console.log(handleNumericalExpressions(expression));
            }
        }
    });
}

function handleNumericalExpressions(expression) {
    const firstParentheses = expression.findIndex((elemenet) => elemenet === ")");
    const matchingParentheses = expression.slice(0, firstParentheses).findLastIndex((elemenet) => elemenet === "(");
    if (matchingParentheses !== -1 && firstParentheses !== -1) {
        const expressionInsideParentheses = expression.slice(matchingParentheses + 2, firstParentheses - 1);
        const result = handleNumericalExpressions(expressionInsideParentheses);
        expression.splice(matchingParentheses, firstParentheses - matchingParentheses + 1, result.toString());
        handleNumericalExpressions(expression);
    }
    const divisibleByZero = (/\/0/).test(expression.join(""));
    if (divisibleByZero) {
        return "ERR DIVBYZERO";
    } else {
        solveTheExpression(expression);
        if (expression.length > 1 | isNaN(expression[0])) {
            return "ERR SYNTAX";
        } else {
            return expression[0];
        }
    }
}

function solveTheExpression(expression) {
    expression = findOperators(expression, "c");
    expression = findOperators(expression, "^");
    expression = findOperators(expression, "/");
    expression = findOperators(expression, "*");
    expression = findOperators(expression, "+");
    expression = findOperators(expression, "-");
    return expression;
}

function findOperators(expression, operator) {
    while (expression.findIndex((elemenet) => elemenet === operator) !== -1) {
        expression = doTheCalculation(expression, operator);
    }
    return expression;
}

function doTheCalculation(expression, operator) {
    const operatorIndex = expression.findIndex((elemenet) => elemenet === operator);
    if (operatorIndex > 0 && operatorIndex < (expression.length - 1)) {
        switch (operator) {
        case "c": {
            const joinTheCharactersbackIntoANumber = expression[operatorIndex - 1] + expression[operatorIndex + 1];
            expression.splice(operatorIndex - 1, 3, joinTheCharactersbackIntoANumber.toString());
            break;
        }
        case "^": {
            const exponentialProduct = expression[operatorIndex - 1] ** expression[operatorIndex + 1];
            expression.splice(operatorIndex - 1, 3, exponentialProduct.toString());
            break;
        }
        case "/": {
            const divisionProduct = parseInt(expression[operatorIndex - 1]) / parseInt(expression[operatorIndex + 1]);
            expression.splice(operatorIndex - 1, 3, divisionProduct.toString());
            break;
        }
        case "*": {
            const MultiplicationProduct = parseInt(expression[operatorIndex - 1]) * parseInt(expression[operatorIndex + 1]);
            expression.splice(operatorIndex - 1, 3, MultiplicationProduct.toString());
            break;
        }
        case "+": {
            const sumProduct = parseInt(expression[operatorIndex - 1]) + parseInt(expression[operatorIndex + 1]);
            expression.splice(operatorIndex - 1, 3, sumProduct.toString());
            break;
        }
        case "-": {
            const subtractionProduct = parseInt(expression[operatorIndex - 1]) - parseInt(expression[operatorIndex + 1]);
            expression.splice(operatorIndex - 1, 3, subtractionProduct.toString());
            break;
        }
        }
    }
    return expression;
}
readNumericalExpressions("./d14.txt");
