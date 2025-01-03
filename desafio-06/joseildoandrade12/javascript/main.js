const readline = require("node:readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const { error } = require("node:console");
const fs = require("node:fs");

function valoresWord(palavraUsuario) {
    fs.readFile("./words.txt", "utf8", (err, texto) => {
        if (err) {
            console.log(error(err));
            return;
        } else {
            const arrayDePalavras = separarTexto(texto);
            compararComLista(arrayDePalavras, palavraUsuario);
        }
    });
}

function compararComLista(lista, valorUsuario) {
    const anagramas = fazendoAnagramas(valorUsuario);
    const anagramasValidos = anagramas.filter((anagrama) =>
        lista.includes(anagrama)
    );

    if (anagramasValidos.length === 0) {
        console.log("nenhum anagrama encontrado");
    } else {
        anagramasValidos.forEach((item) => {
            console.log(item);
        });
    }
}

function pegandoValoresUsuario() {
    rl.question("Informe a palavra: ", (value) => {
        const palavraResetada = resetPalavra(value);
        const validacaoValor = validarValores(palavraResetada);
        if (validacaoValor) {
            valoresWord(palavraResetada);
        } else {
            pegandoValoresUsuario();
        }
    });
}
pegandoValoresUsuario();

function resetPalavra(palavra) {
    return palavra.toUpperCase().split(" ").join("");
}

function validarValores(palavra) {
    const validarTamanho = palavra.length <= 16;
    const validarCaracteres = /^[A-Za-z_]+$/gi.test(palavra);

    if (validarTamanho && validarCaracteres) return true;
    else {
        console.log(`Digite palavras sem acentos e sem pontuações`);
        return false;
    }
}

function fazendoAnagramas(value) {
    const arrayPalavra = value.split("");
    const anagramas = [];

    permutar(arrayPalavra, 0, arrayPalavra.length - 1, anagramas);
    return anagramas;
}

function permutar(arr, l, indexArray, anagramas) {
    if (l === indexArray) {
        anagramas.push(arr.join(""));
    } else {
        for (let i = l; i <= indexArray; i++) {
            [arr[l], arr[i]] = [arr[i], arr[l]];
            permutar(arr, l + 1, indexArray, anagramas);
            [arr[l], arr[i]] = [arr[i], arr[l]];
        }
    }
}

function separarTexto(texto) {
    return texto.split(/\n/);
}
