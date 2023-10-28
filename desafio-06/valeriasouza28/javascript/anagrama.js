const fs = require("fs");
const fileName = "./words.txt";
const readline = require("readline-sync");
const word = readline.question("Digite uma palavra: ");
const characterInputCheck = /^[a-zA-Z\s]+$/;

function readFile(fileName) {
    try {
        const data = fs.readFileSync(fileName, "utf8");
        return data;
    } catch (error) {
        if (error.code === "ENOENT") {
            console.error("O arquivo não foi encontrado.");
        } else {
            console.error("Ocorreu um erro ao ler o arquivo:", error.message);
        }
    }
}

function normalizeWords(word) {
    const normalized = word
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toUpperCase();

    return normalized.toString();
}

function testAnagram(word1, word2) {
    if (Object.keys(word1).length !== Object.keys(word2).length) {
        return false;
    }
    for (const letter in word1) {
        if (word1[letter] !== word2[letter]) {
            return false;
        }
    }
    return true;
}

function inspectWord(word) {
    const count = {};
    for (let i = 0; i < word.length; i++) {
        const letter = word[i];
        count[letter] = (count[letter] || 0) + 1;
    }

    const newObject = {};

    Object.keys(count).forEach((key) => {
        if (key !== " ") {
            newObject[key] = count[key];
        }
    });

    return newObject;
}

const fileData = readFile(fileName);

if (fileData) {
    const foundWords = [];
    const lines = fileData.split("\n");
    const word1 = inspectWord(normalizeWords(word));

    try {
        if (!characterInputCheck.test(word)) {
            throw new Error("A palavra digitada contém caracteres inválidos.");
        } else if (word.length > 16) {
            throw new Error("Digite uma palavra com menos de 16 caracteres.");
        } else {
            for (const line of lines) {
                const word2 = inspectWord(normalizeWords(line));
                const isAnagram = testAnagram(word1, word2);
                if (isAnagram) {
                    foundWords.push(line);
                }
            }
        }
        foundWords.forEach((element) => {
            console.log(element);
        });
    } catch (error) {
        if (error.message === "A palavra digitada contém caracteres inválidos.") {
            console.error(`Erro: ${error.message}`);
        } else if (error.message === "Digite uma palavra com menos de 16 caracteres.") {
            console.error(`Erro: ${error.message}`);
        } else {
            console.error(error);
        }
    }
}
