const primos = [];

for (let i = 2; i <= 10000; i++) {
    let isPrimo = true;
    if (i % 2 !== 0) {
        for (let st = 2; st <= Math.floor(Math.sqrt(i)); st++) {
            if (i % st === 0) {
                isPrimo = false;
                break;
            }
        }
        if (isPrimo) { primos.push(i); };
    }
}

console.log(primos);
