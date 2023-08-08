const fs = require("fs");
const nomeDoArquivo = "./words.txt";


function procurarAnagrama(palavra) {
    try {

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
            const palavraArquivo = linha.trim();
            const palavra2 = inspecionarPalavra(normalizarPalavras(linha));
            const testaAnagrama = testaSeAnagrama(palavra1, palavra2);

            if (testaAnagrama) {
                palavrasEncontradas.push(linha);
            }
        }
        return palavrasEncontradas;
    } catch (err) {
        if (err.code === "ENOENT") {
            console.error(
                `Erro ao encontrar o arquivo ${nomeDoArquivo}. Por favor, verifique se o nome do arquivo está correto.`
            );
            return false;
        } else {
            return false;
        }
    }
}

const procurandoAnagrama = procurarAnagrama("listen");
console.log(procurandoAnagrama);
