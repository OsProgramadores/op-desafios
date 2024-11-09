function imprimePrimo(numero) {
    let numeroInicial = 2;
    let contadorDeDivisoes = 0;
    while (numeroInicial <= Math.sqrt(numero)) {
        if (numero % numeroInicial === 0) {
            contadorDeDivisoes++;
        }
        numeroInicial++;
    }

    if (contadorDeDivisoes === 0) {
        console.log(numero);
    }
}

for (let i = 3; i <= 10000; i += 2) {
    imprimePrimo(i);
}
