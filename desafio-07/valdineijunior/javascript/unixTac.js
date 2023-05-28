const fs = require("fs");
const readline = require("readline");

function countLines(filePath) {
    return new Promise((resolve, reject) => {
        let lineCount = 0;

        const stream = fs.createReadStream(filePath);
        const rl = readline.createInterface({
            input: stream,
            crlfDelay: Infinity
        });

        rl.on("line", () => {
            lineCount++;
        });

        rl.on("close", () => {
            resolve(lineCount);
        });

        stream.on("error", (error) => {
            reject(error);
        });
    });
}

function getLines(filePath, startLine, endLine) {
    return new Promise((resolve, reject) => {
        const lines = [];
        let lineCount = 0;

        const stream = fs.createReadStream(filePath);
        const rl = readline.createInterface({
            input: stream,
            crlfDelay: Infinity
        });

        rl.on("line", (line) => {
            lineCount++;
            if (lineCount >= startLine && lineCount <= endLine) {
                lines.push(line);
            }
        });

        rl.on("close", () => {
            resolve(lines);
        });

        stream.on("error", (error) => {
            reject(error);
        });
    });
}

async function printLines(filePath, lineCount) {
    const batchSize = 425000; // Define um tamanho do lote para impressão que funcione com 512M de memória

    for (let start = lineCount; start > 0; start -= batchSize) {
        const end = Math.max(start - batchSize + 1, 1);
        try {
            const lines = await getLines(filePath, end, start);
            lines.reverse();
            console.log(lines.join("\n"));
        } catch (error) {
            console.error("Error:", error);
        }
    }
}

async function processFile(filePath) {
    if (!fs.existsSync(filePath)) {
        console.error("Erro: O arquivo especificado não existe.");
        process.exit(1);
    }

    try {
        const lineCount = await countLines(filePath);
        await printLines(filePath, lineCount);
    } catch (error) {
        console.error("Error:", error);
    }
}

const filePath = process.argv[2];
if (!filePath) {
    console.error("Erro: Caminho do arquivo não fornecido. Utilize 'node unixTac.js arquivo.txt'");
    process.exit(1);
}

processFile(filePath);
