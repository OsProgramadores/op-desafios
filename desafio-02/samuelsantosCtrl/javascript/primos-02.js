function verifyPrime(N) { // retorna true para numeros primos
    // trata alguns casos especiais
    if (N === 1) return false;
    if (N <= 3) return true;
    if (N % 2 === 0 || N % 3 === 0) { // pula multiplos de 2 e 3
        return false;
    }
    //verifica numeros ate a raiz quadrada do numero N
    for (let i = 2; i * i <= N; i++) {
        if (N % i === 0) {
            return false;
        }
    }
    return true;
}

const MAX_VALUE = 10000;
const num = [];
for (let i = 1; i <= MAX_VALUE; i++) {
    num.push(i);
}
const resultado = num.filter(verifyPrime); //funcao que filtra numeros primos
for (let i = 0; i <= resultado.length - 1; i++) {
    console.log(resultado[i]); //exibi os numeros encontrados
};
