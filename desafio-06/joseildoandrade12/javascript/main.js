const arrayWords = [];
const fs = require("node:fs");
fs.readFile("./words.txt", "utf8", repostaWord);

function repostaWord(err, data) {
    if (err) {
        console.log(err);
    }
    arrayWords.push(...separarTexto(data));
    return data;
}

function separarTexto(texto) {
    return texto.split(/\n/).map((word) => word.trim());
}

const { createInterface } = require("node:readline");
const rl = createInterface({
    input: process.stdin,
    output: process.stdout
});

function questionUsuario() {
    rl.question("Digite uma palavra: ", (palavra) => {
        if (validarPalavra(palavra)) {
            const palavraResetada = resetarPalavra(palavra);
            const arrayValoresComparados = compararValores(palavraResetada, arrayWords);
            const valoresCorretosWord = arrayValoresComparados.filter((item) => {
                return verificarRepeticaoLetras(item, palavraResetada) === 0;
            });
            const combinacoesPalavras = fazerCombinacoes(valoresCorretosWord, palavraResetada);
            const valoresCorretos = combinacoesPalavras.filter((item) => {
                const itemResetado = item.split(" ").join("");
                return verificarRepeticaoLetras(itemResetado, palavraResetada) === 0;
            });
            for (const palavra of valoresCorretos) {
                console.log(palavra);
            }
            rl.close();
        } else {
            questionUsuario();
        }
    });
}
questionUsuario();

const validarPalavra = (palavra) => {
    const palavraResetada = palavra.split(" ").join("");
    const validarCaracteres = /^[A-Za-z]+$/gi.test(palavraResetada);
    if (validarCaracteres) {
        return true;
    } else {
        console.log("Digite apenas palavras(sem acentos e sem pontuações)");
        return false;
    }
};

const resetarPalavra = (palavra) => {
    return palavra.toUpperCase().replace(" ", "");
};

const compararValores = (palavra, listaWords) => {
    const regex = new RegExp(`^[${palavra}]+$`, "g");
    const palavrasComparadas = listaWords.filter((itemWords) => {
        return itemWords.length <= palavra.length && regex.test(itemWords);
    });
    return palavrasComparadas;
};

const verificarRepeticaoLetras = (palavraWords, palavraUser) => {
    const arrayPalavra = palavraUser.split("");
    const arrayPalavraWords = palavraWords.split("");
    arrayPalavra.forEach((letra) => {
        const index = arrayPalavraWords.indexOf(letra);
        if (index > -1) {
            arrayPalavraWords.splice(index, 1);
        }
    });
    return arrayPalavraWords.length;
};

const fazerCombinacoes = (array, palavraUser) => {
    const resultados = [];

    const combinar = (palavra, arrayPalavra) => {
        const palavraResetada = palavra.split(" ").join("");
        if (palavraResetada.length === palavraUser.length) {
            resultados.push(palavra);
        } else if (palavraResetada.length < palavraUser.length) {
            for (let i = 0; i < arrayPalavra.length; i++) {
                combinar(palavra + " " + arrayPalavra[i], arrayPalavra);
            }
        }
    };

    for (let i = 0; i < array.length; i++) {
        const palavra = array[i];
        if (palavra.length === palavraUser.length) {
            resultados.push(palavra);
        } else if (palavra.length < palavraUser.length) {
            combinar(palavra, array);
        }
    }
    return resultados;
};
