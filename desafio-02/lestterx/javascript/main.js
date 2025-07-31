const primos = [];

for (let i = 2; i <= 10000; i++) {
    let isPrimo = true;
    if (i % 2 !== 0) {
        const raizQuadrada = Math.floor(Math.sqrt(i))
        for (let st = 2; st <= raizQuadrada; st++) {
            if (i % st === 0) {
                isPrimo = false;
                break;
            }
        }
        if (isPrimo) {
            primos.push(i);
        };
    }
}

for (let i = 0; i < primos.length; i++) {
    console.log(`Primo Nº${i + 1}: ${primos.at(i)}`);
}
