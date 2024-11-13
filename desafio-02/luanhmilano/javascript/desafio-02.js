function imprimePrimo(numero) {
    let numeroInicial = 2;
    let isDivisivel = false;
    while (numeroInicial <= Math.sqrt(numero)) {
        if (numero % numeroInicial === 0) {
            isDivisivel = true;
            break;
        }
        numeroInicial++;
    }

    if (!isDivisivel) {
        console.log(numero);
    }
}

for (let i = 3; i <= 10000; i += 2) {
    imprimePrimo(i);
}
