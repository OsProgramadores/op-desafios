function ehPrimo(numero) {
    if (numero <= 1) return false;
    for (let divisor = 2; divisor <= Math.sqrt(numero); divisor++) {
        if (numero % divisor === 0) return false;
    }
    return true;
}

const numerosPrimos = [];

for (let numero = 1; numero <= 10000; numero++) {
    if (ehPrimo(numero)) {
        numerosPrimos.push(numero);
    }
}
console.log("Números primos entre 1 e 10000:");
console.log(numerosPrimos.join(", "));
console.log(`Total de números primos encontrados: ${numerosPrimos.length}`);
