function crivo(limite) {
    const numNaoPrimos = new Array(limite + 1).fill(false);
    // marcamos os múltiplos, só até a raiz quadrada do limite
    for (let numero = 2; numero * numero <= limite; numero++) {
        if (!numNaoPrimos[numero]) {
            for (
                let multiplo = numero * numero;
                multiplo <= limite;
                multiplo += numero
            ) {
                numNaoPrimos[multiplo] = true;
            }
        }
    }

    // adicionamos todos os primos encontrados ao array
    const primos = [];
    for (let numero = 2; numero <= limite; numero++) {
        if (!numNaoPrimos[numero]) {
            primos.push(numero);
        }
    }
    return primos;
}

const primos = crivo(1000);
console.log(primos.join(", "));
