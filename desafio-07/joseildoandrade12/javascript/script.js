const fs = require("fs");
const readline = require("readline");

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
    const size = 400000;
    try {
        for (let initLines = quantityLines; initLines > 0; initLines -= size) {
            const arrayLines = await pullData(path, quantityLines, initLines);
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
