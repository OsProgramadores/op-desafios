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
    let [numerator, denominator] = line.split("/");
    numerator = parseInt(numerator);
    denominator = parseInt(denominator);

    if (!validateValues(numerator, denominator)) {
        return console.log("ERR");
    } else {
        simplifyFraction(numerator, denominator);
    }
}

function validateValues(numerator, denominator) {
    if (numerator === 0 || denominator === 0) {
        return false;
    } else if (!denominator) {
        return true;
    } else if (isNaN(numerator) !== false || isNaN(denominator) !== false) {
        return false;
    } else if (Number.isInteger(numerator) !== true || Number.isInteger(denominator) !== true) {
        return false;
    } else {
        return true;
    }
}

function simplifyFraction(numerator, denominator) {
    if (!denominator) {
        console.log(numerator);
    } else if (numerator === denominator) {
        console.log("1");
    } else if (denominator === 1) {
        console.log(numerator);
    } else if (numerator < denominator) {
        if (denominator % numerator === 0) {
            console.log(`1/${denominator / numerator}`);
        } else {
            let half = Math.ceil(numerator / 2);

            for (half; half > 0; half--) {
                if (numerator % half === 0 && denominator % half === 0) {
                    console.log(`${numerator / half}/${denominator / half}`);
                    break;
                }
            }
        }
    } else if (numerator > denominator) {
        if (numerator % denominator === 0) {
            console.log(`${numerator / denominator}`);
        } else {
            let i = 0;
            while (numerator > denominator) {
                numerator -= denominator;
                i++;
            }
            console.log(`${i} ${numerator}/${denominator}`);
        }
    }
}

const fileName = process.argv[2];
readFileByLine(fileName);
