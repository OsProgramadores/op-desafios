const primos = [];

for (let numero = 2; numero <= 1000; numero++) {
    let ehPrimo = true;
    const raiz = Math.sqrt(numero);
    for (let i = 0; i < primos.length && primos[i] <= raiz; i++) {
        if (numero % primos[i] === 0) {
            ehPrimo = false;
            break;
        }
    }
    if (ehPrimo) {
        primos.push(numero);
        console.log(numero);
    }
};
