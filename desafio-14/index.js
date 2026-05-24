const fs = require('fs');

function main() {

    const arquivo = './desafio-14/expressoes.txt';

    const linhas = fs.readFileSync(arquivo, 'utf8').split('\n');

    linhas.forEach(linha => {

        linha = linha.trim();

        if (linha === '') return;

        try {
            const resultado = avaliarExpressao(linha);
            console.log(resultado);
        } catch (e) {
            console.log(e.message);
        }

    });
}

// ================= TOKENIZER =================
function tokenize(expr) {
    const tokens = [];
    let num = '';

    for (let c of expr) {

        if (c === ' ') continue;

        if (isDigit(c)) {
            num += c;
        } else {
            if (num !== '') {
                tokens.push(num);
                num = '';
            }
            tokens.push(c);
        }
    }

    if (num !== '') tokens.push(num);

    return tokens;
}

function isDigit(c) {
    return c >= '0' && c <= '9';
}

// ================= PRIORIDADE =================
function prec(op) {
    if (op === '^') return 3;
    if (op === '*' || op === '/') return 2;
    if (op === '+' || op === '-') return 1;
    return 0;
}

function rightAssoc(op) {
    return op === '^';
}

// ================= SHUNTING YARD =================
function toRPN(tokens) {
    const output = [];
    const ops = [];

    for (let t of tokens) {

        if (!isNaN(t)) {
            output.push(Number(t));
        }

        else if (t === '+' || t === '-' || t === '*' || t === '/' || t === '^') {

            while (
                ops.length &&
                ops[ops.length - 1] !== '(' &&
                (
                    prec(ops[ops.length - 1]) > prec(t) ||
                    (prec(ops[ops.length - 1]) === prec(t) && !rightAssoc(t))
                )
            ) {
                output.push(ops.pop());
            }

            ops.push(t);
        }

        else if (t === '(') {
            ops.push(t);
        }

        else if (t === ')') {

            let found = false;

            while (ops.length) {
                const op = ops.pop();
                if (op === '(') {
                    found = true;
                    break;
                }
                output.push(op);
            }

            if (!found) throw new Error('ERR SYNTAX');
        }

        else {
            throw new Error('ERR SYNTAX');
        }
    }

    while (ops.length) {
        const op = ops.pop();
        if (op === '(' || op === ')') throw new Error('ERR SYNTAX');
        output.push(op);
    }

    return output;
}

// ================= AVALIA RPN =================
function evalRPN(rpn) {

    const stack = [];

    for (let t of rpn) {

        if (typeof t === 'number') {
            stack.push(t);
        } else {

            const b = stack.pop();
            const a = stack.pop();

            if (a === undefined || b === undefined) {
                throw new Error('ERR SYNTAX');
            }

            let res;

            if (t === '+') res = a + b;
            if (t === '-') res = a - b;
            if (t === '*') res = a * b;

            if (t === '/') {
                if (b === 0) throw new Error('ERR DIVBYZERO');
                res = a / b;
            }

            if (t === '^') {
                res = Math.pow(a, b);
            }

            stack.push(res);
        }
    }

    if (stack.length !== 1) {
        throw new Error('ERR SYNTAX');
    }

    return stack[0];
}

// ================= FUNÇÃO PRINCIPAL =================
function avaliarExpressao(expr) {
    const tokens = tokenize(expr);
    const rpn = toRPN(tokens);
    return evalRPN(rpn);
}

main();