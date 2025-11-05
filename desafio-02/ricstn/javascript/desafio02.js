const numeros = [];
for (let i = 1; i <= 10000; i++) {
    let contador = 0;
    for (let j = i; j > 0; j--) {
        if (i % j === 0) {
            contador += 1;
        }
        if (contador > 2) {
            break;
        }
    }
    if (contador === 2) {
        numeros.push(i);
    }
}
console.log(numeros);
