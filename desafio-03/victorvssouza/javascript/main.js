const readline = require("readline");

function capturaDados(callback) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Digite o valor inicial: ", (valorInicial) => {
        rl.question("Digite o valor final: ", (valorFinal) => {
            rl.close();
            callback(Number(valorInicial), Number(valorFinal));
        });
    });
}

function validacaoDados(valorInicial, valorFinal) {
    if (!Number.isInteger(valorInicial) || !Number.isInteger(valorFinal)) {
        throw new Error("Os valores devem ser números inteiros.");
    }
    if (valorInicial < 0 || valorFinal < 0) {
        throw new Error("Os valores devem ser números positivos.");
    }
    if (valorInicial > valorFinal) {
        throw new Error("O valor final deve ser igual ou maior que o valor inicial.");
    }
}

function validacaoPolindromo(numeroSelecionado) {
    const stringNumeroSelecionado = numeroSelecionado.toString();
    return stringNumeroSelecionado === stringNumeroSelecionado.split("").reverse().join("");
}

function buscaPolindromo(valorInicial, valorFinal) {
    const palindromos = [];
    for (let numero = valorInicial; numero <= valorFinal; numero++) {
        if (validacaoPolindromo(numero)) {
            palindromos.push(numero);
        }
    }
    return palindromos;
}

function main() {
    try {
        capturaDados((valorInicial, valorFinal) => {
            try {
                validacaoDados(valorInicial, valorFinal);
                const palindromos = buscaPolindromo(valorInicial, valorFinal);
                console.log(`Números palíndromos entre ${valorInicial} e ${valorFinal}: ${palindromos.join(", ")}`);
            } catch (error) {
                console.error(error.message);
            }
        });
    } catch (error) {
        console.error(error.message);
    }
}

main();
