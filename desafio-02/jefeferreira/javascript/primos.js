function crivo(limite) {
    const primos = [];
    const numNaoPrimos = new Array(limite + 1).fill(false);

    for (let numero = 2; numero <= limite; numero++) {
        if (!numNaoPrimos[numero]) {
            primos.push(numero);

            // Marca os múltiplos desse primo como não primos
            for (
                let multiplo = numero * numero;
                multiplo <= limite;
                multiplo += numero
            ) {
                numNaoPrimos[multiplo] = true;
            }
        }
    }
    return primos;
}

const primos = crivo(10000);
console.log(primos.join(", "));
