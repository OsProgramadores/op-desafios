const primos = [];
const naoPrimos = [];

for (let numero = 2; numero <= 1000; numero++) {
    let ehPrimo = true;
    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
            ehPrimo = false;
            break;
        }
    }
    if (ehPrimo) {
        primos.push(numero);
    } else {
        naoPrimos.push(numero);
    }
}

console.log(primos);
console.log(naoPrimos);
