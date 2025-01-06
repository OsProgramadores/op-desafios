// métodos de node
const readline = require("node:readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const { error } = require("node:console");
const fs = require("node:fs");

// puxa os valores de word e retora uma array com os valores
function valoresWord(palavraUsuario) {
    fs.readFile("./words.txt", "utf8", (err, texto) => {
        if (err) {
            console.log(error(err));
        } else {
            const arrayDePalavras = separarTexto(texto);
            compararComLista(arrayDePalavras, palavraUsuario);
        }
    });
}

// Recebe os valores do usuário e armazena ele
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

// compara os anagramas da palavra passada pelo usuário com a lista word e retorna uma lista
function compararComLista(lista, valorUsuario) {
    const arrayItensAnagrama = [];
    const anagramas = fazendoAnagramas(valorUsuario);
    anagramas.forEach((anagrama) => {
        lista.forEach((item) => {
            if (anagrama.includes(item) && !arrayItensAnagrama.includes(item)) {
                arrayItensAnagrama.push(item.trim());
            }
        });
    });

    const arrayJuncoes = encontrarCombinações(
        arrayItensAnagrama,
        valorUsuario.length
    );

    arrayJuncoes.sort().forEach((item) => {
        console.log(item);
    });
}

// junta os valores até chegar no tamanho da palavra passada pelo usuário
function encontrarCombinações(palavras, tamanhoPalavra) {
    const resultados = new Set();
    function combinar(palavra, array) {
        if (palavra.length === tamanhoPalavra) {
            resultados.add(palavra);
        } else if (palavra.length < tamanhoPalavra) {
            for (let i = 0; i < array.length; i++) {
                combinar(palavra + array[i], array.slice(i + 1));
                combinar(array[i] + palavra, array.slice(i + 1));
            }
        }
    }

    for (let i = 0; i < palavras.length; i++) {
        const palavra = palavras[i];
        if (palavra.length === tamanhoPalavra) {
            resultados.add(palavra);
        } else if (palavra.length < tamanhoPalavra) {
            combinar(palavra, palavras.slice(i + 1));
        }
    }
    return Array.from(resultados);
}

// reseta valor passado pelo usuário deixando ele sem espaços e em maiúsculo
function resetPalavra(palavra) {
    return palavra.toUpperCase().split(" ").join("");
}

// Valida os valores passados pelo usuário
function validarValores(palavra) {
    const validarCaracteres = /^[A-Za-z]+$/gi.test(palavra);
    if (validarCaracteres) return true;
    else {
        console.log("Digite apenas palavras(sem acentos e sem pontuações)");
        return false;
    }
}

// função para puxar os valores de anagramas passados pelo usuário
function fazendoAnagramas(value) {
    const arrayPalavra = value.split("");
    const anagramas = [];

    permutar(arrayPalavra, 0, arrayPalavra.length - 1, anagramas);
    return anagramas;
}

// permutação dos valores utilizados pelo usuário
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

// Retorna os valores da lista word dentro de uma array
function separarTexto(texto) {
    return texto.split(/\n/);
}
