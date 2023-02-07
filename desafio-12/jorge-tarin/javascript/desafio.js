const fs = require("fs");
const readline = require("readline");

async function readFileByLine(file) {
    const fileStream = fs.createReadStream(file);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        captureValues(line);
    }
}

function captureValues(line) {
    const number = BigInt(line);
    const value = calculatePower(number);

    if (value[0] === "true") {
        console.log(`${number} true ${value[1]}`);
    } else {
        console.log(`${number} false`);
    }
}

function calculatePower(number) {
    let exponent = 0;

    while (number >= 1n) {
        if (number === 1n) {
            return ["true", exponent];
        } else if (number % 2n !== 0n) {
            return ["false", exponent];
        }
        number = number / 2n;
        exponent++;
    }

    return ["false", exponent];
}

const fileName = process.argv[2];
readFileByLine(fileName);
