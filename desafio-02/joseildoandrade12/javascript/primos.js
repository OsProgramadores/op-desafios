function numerosPrimos(max) {
    const arrayNumerosPrimos = [];
    for (let num = 2; num <= max; num++) {
        let numeroPrimo = true;
        for (let divisor = 2; divisor < num; divisor++) {
            if (num % divisor === 0) {
                numeroPrimo = false;
            }
        }
        if (numeroPrimo === true) {
            arrayNumerosPrimos.push(num);
        }
    }
    return arrayNumerosPrimos;
}

console.log(numerosPrimos(10000));
