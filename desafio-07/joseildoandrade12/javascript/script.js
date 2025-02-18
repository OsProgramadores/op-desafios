const fs = require("fs");
const readline = require("readline");
const { start } = require("repl");

async function commandInline() {
    const command = process.argv.slice(2);
    if (command[0]) {
        try {
            const quantityLines = await countingLines(command[0]);
            await pushLines(command[0], quantityLines);
        } catch (err) {
            console.error(err);
        }
    } else {
        console.log("Use: node script.js <caminho_do_arquivo>");
    }
}
commandInline();

async function pushLines(path, quantityLines) {
    const size = 512000;
    for (let finallyLine = quantityLines; finallyLine > 0; finallyLine -= size) {
        try {
            const initLines = Math.max(finallyLine - size + 1, 1);
            const arrayLines = await pullData(path, initLines, finallyLine);
            arrayLines.reverse();
            console.log(arrayLines.join("\n"));
        } catch (error) {
            console.log(error);
        }
    }
}

function pullData(path, initLines, finallyLine) {
    return new Promise((resolve, reject) => {
        const arrayItens = [];
        let indexLine = 0;
        const fileStream = fs.createReadStream(path);
        const reader = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        reader.on("error", (err) => {
            console.log("Arquivo não encontrado!");
            reject(err);
        });

        reader.on("line", (line) => {
            indexLine++;
            if (indexLine >= initLines && indexLine <= finallyLine) {
                arrayItens.push(line);
            }
        });

        reader.on("close", () => {
            resolve(arrayItens);
        });
    });
}

async function countingLines(path) {
    return new Promise((resolve, reject) => {
        let quantityLine = 0;
        const fileStream = fs.createReadStream(path);
        const reader = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });
        reader.on("error", (err) => {
            console.log("Arquivo não encontrado!");
            reject(err);
        });

        reader.on("line", () => {
            quantityLine++;
        });

        reader.on("close", () => {
            resolve(quantityLine);
        });
    });
}
