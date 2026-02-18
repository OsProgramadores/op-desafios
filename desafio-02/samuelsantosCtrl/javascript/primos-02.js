const notIsPrime = []; // multiplos de primos nao podem ser primos
const num = []; // inicializacao do array de 1 - 10k

for (let i = 1; i <= 10000; i++) {
    num.push(i);
}

function notOnList(number) {
    if (notIsPrime.includes(number)) {
        return false;
    } else {
        return true;
    }
}

function descarteMultiplos(N) {
    while (N < 10000) {
        N *= 2;
        notIsPrime.push(N);
    }
}

function verifyPrime(N) {
    for (let i = 2; i < N; i++) {
        if (N % i === 0) {
            descarteMultiplos(N);
            return false;
        }
    }
    return true;
}

function findPrimes(value) {
    if (notOnList(value)) { // passou pelo teste do descarte, agora a parte principal
        if (verifyPrime(value)) {
            console.log(value); // retorna numeros primos
        }
    }
}

num.forEach(findPrimes);