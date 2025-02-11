const fs = require("fs");
const readline = require("readline");

async function commandInline() {
    const command = process.argv.slice(2);
    if (command[0] === "tac") {
        if (command[1]) {
            try {
                const quantityLines = await countingLines(command[1]);
                await pushLines(command[1], quantityLines);
            } catch (err) {
                console.error(err);
            }
        } else {
            console.log("Use: node script.js tac <caminho_do_arquivo>");
        }
    } else {
        console.log("Comando inválido");
    }
}
commandInline();

async function pushLines(path, quantityLines) {
    const size = 512000;
    try {
        for (let finallyLine = quantityLines; quantityLines > 0; finallyLine -= size) {
            const arrayLines = await pullData(path, quantityLines, finallyLine);
            arrayLines.reverse();
            arrayLines.forEach((line) => {
                console.log(line);
            });
        }
    } catch (error) {
        console.log(error);
    }
}

function pullData(path, quantityLines, finallyLine) {
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
            if (indexLine > finallyLine && indexLine < quantityLines) {
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
        const fileStream = fs.createReadStream(path, { encoding: "utf8" });
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
