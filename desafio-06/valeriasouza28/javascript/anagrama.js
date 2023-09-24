const fs = require("fs");
const nomeDoArquivo = "./words.txt";
const readline = require("readline-sync");
const palavra = readline.question("Digite uma palavra : ");

function normalizarPalavras(palavra) {
    const normaliza = palavra
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
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
const palavra1 = inspecionarPalavra(normalizarPalavras(palavra));
const palavrasEncontradas = [];
for (const linha of linhas) {
    const palavra2 = inspecionarPalavra(normalizarPalavras(linha));
    const testaAnagrama = testaSeAnagrama(palavra1, palavra2);
    if (testaAnagrama) {
        palavrasEncontradas.push(linha);
    }
}

palavrasEncontradas.forEach(element => {
    console.log(element);
});
