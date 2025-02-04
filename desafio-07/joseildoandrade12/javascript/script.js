const fs = require("fs");

async function commandInline() {
    const command = process.argv.slice(2);
    if (command[0] === "tac") {
        try {
            const arr = await pullData(command[1]);
            arr.reverse();
            for (const item of arr) {
                console.log(item);
            }
        } catch (err) {
            console.error(err);
        }
    } else {
        console.log("Comando inválido");
    }
}
commandInline();

function pullData(path) {
    return new Promise((resolve, reject) => {
        const arrayItens = [];
        const reader = fs.createReadStream(path, {
            highWaterMark: 512000000,
            encoding: "utf-8"
        });

        reader.on("error", (err) => {
            console.log("Arquivo não encontrado!");
            reject(err);
        });

        reader.on("data", (chunck) => {
            const lineReset = breakText(chunck);
            arrayItens.push(...lineReset);
        });

        reader.on("end", () => {
            resolve(arrayItens);
        });
    });
}

const breakText = (text) => {
    return text
        .trim()
        .split(/\n/)
        .map((item) => item.trim());
};
