function primo(numero = 10000) {

    let primos = [2, 3, 5, 7];
    for (let i = 8; i <= numero; i++) {
        if (Number.isInteger(i % 2) === false && Number.isInteger(i % 3) === false && Number.isInteger(i % 5) === false && Number.isInteger(i % 7) === false) {
            primos.push(i);
        }
    }
    return primos;
}

let j = 11;
console.log(Number.isInteger(j % 2));