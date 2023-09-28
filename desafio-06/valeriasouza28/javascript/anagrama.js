const fs = require("fs");
const nomeDoArquivo = "./words.txt";
const readline = require("readline-sync");
const palavra = readline.question("Digite uma palavra : ");
const verificaInputCaracteres = /^[a-zA-Z\s]*$/;
const { Writable } = require("stream");

function normalizarPalavras(palavra) {
    const normaliza = palavra
        .normalize("NFD")
        .replace(/[\u0300-\u036f\s]/g, "")
        .toUpperCase();

    return normaliza.toString();
}
function testaSeAnagrama(palavra1, palavra2) {
    if (Object.keys(palavra1).length !== Object.keys(palavra2).length) {
        return false;
    }
    for (const letter in palavra1) {
        if (palavra1[letter] !== palavra2[letter]) {
            return false;
        }
    }
    return true;
}

function inspecionarPalavra(palavra) {
    const count = {};
    for (let i = 0; i < palavra.length; i++) {
        const letter = palavra[i];
        count[letter] = (count[letter] || 0) + 1;
    }
    return count;
}
const linhas = fs.readFileSync(nomeDoArquivo, "utf8").split("\n");
const palavrasEncontradas = [];
try {
    if (!verificaInputCaracteres.test(palavra)) {
        throw new Error("A palavra digitada contém caracteres inválidos.");
    } else if (palavra.length > 16) {
        throw new Error("Digite uma palavra com menos de 16 caracteres.");
    } else {
        const palavraNormalizada = normalizarPalavras(palavra);
        const palavra1 = inspecionarPalavra(palavraNormalizada);

        for (const linha of linhas) {
            const palavra2 = inspecionarPalavra(normalizarPalavras(linha));
            const testaAnagrama = testaSeAnagrama(palavra1, palavra2);
            if (testaAnagrama) {
                palavrasEncontradas.push(linha);
            }
        }
    }

    const writeSteam = new Writable({
        write(chunk, encoding, callback) {
            console.log(chunk.toString());
            callback();
        }
    });

    palavrasEncontradas.forEach(element => {
        writeSteam.write(element + "\n");
    });
} catch (error) {
    if (error.message === "A palavra digitada contém caracteres inválidos.") {
        console.error(`Erro : ${error.message}`);
    } else if (
        error.message === "Digite uma palavra com menos de 16 caracteres."
    ) {
        console.error(`Erro : ${error.message}`);
    } else {
        console.error(error);
    }
}
