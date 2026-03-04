function verifyPrime(N) { // retorna true para numeros primos
    // trata alguns casos especiais
    if (N === 1) return false;
    if (N <= 3) return true;
    if (N % 2 === 0 || N % 3 === 0) { // pula multiplos de 2 e 3
        return false;
    }
    // verifica numeros ate a raiz quadrada do numero N
    for (let i = 5; i * i <= N; i += 6) {
        // novo teste na forma se 6*k ± 1
        if (N % i === 0 || N % (i + 2) === 0) {
            return false;
        }
    }
    return true;
}

const MAX_VALUE = 10000;
const resultado = [];
for (let i = 1; i <= MAX_VALUE; i++) {
    if (verifyPrime(i) === true) {
        resultado.push(i);
    }
}
resultado.forEach((element) => console.log(element));
