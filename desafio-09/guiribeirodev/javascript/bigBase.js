const fs = require("fs");
const readline = require("readline");

function checkIfIsValid(entryBase, outputBase, entryValue) {
    const characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    if ((entryBase && outputBase < 2) || (entryBase && outputBase > 62)) {
        return false;
    } else if (parseInt(entryValue) < 0) {
        return false;
    }

    for (const char of entryValue) {
        const x = characters.indexOf(char);
        if (x >= entryBase) {
            return false;
        }
    }

    return true;
}

function convertToDecimalBase(entryBase, entryValue) {
    const characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const base = BigInt(entryBase);
    let decimal = BigInt(0);

    for (let i = 0; i < entryValue.length; i++) {
        const character = entryValue[i];
        const value = BigInt(characters.indexOf(character));
        decimal = decimal * base + value;
    }
    return decimal;
}

function convertToOutputBase(decimal, outputBase) {
    const characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    let allRemains = [];

    while (decimal !== 0n) {
        const remainder = parseInt(decimal % BigInt(outputBase));

        decimal = decimal / BigInt(outputBase);

        allRemains = [remainder, ...allRemains];
    }

    const convertedValue = allRemains.map((value) => {
        value = characters[value];
        return value;
    });

    return convertedValue.join("");
}

async function readFile(file) {
    const fileStream = fs.createReadStream(file);

    const rl = readline.createInterface({
        input: fileStream
    });

    rl.on("line", (line) => {
        const [entryBase, outputBase, entryValue] = line.split(" ");
        const limit = BigInt(convertToDecimalBase(62, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        );

        if (!checkIfIsValid(entryBase, outputBase, entryValue)) {
            console.log("???");
            return;
        }

        if (entryValue === "0") {
            console.log("0");
            return;
        }

        if (entryBase === "10") {
            const decimal = BigInt(entryValue);
            const convertedValue = convertToOutputBase(decimal, outputBase);
            console.log(convertedValue);
            return;
        }

        const decimal = convertToDecimalBase(entryBase, entryValue);

        if (decimal > limit) {
            console.log("???");
            return;
        }

        const convertedValue = convertToOutputBase(decimal, outputBase);

        console.log(convertedValue);
    });
}

function main() {
    const file = process.argv[2];

    readFile(file);
}

main();
