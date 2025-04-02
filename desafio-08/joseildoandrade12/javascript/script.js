const readline = require("readline");
const fs = require("fs");

async function commandInline() {
    const command = process.argv.slice(2);
    if (command[0]) {
        try {
            readFileByLine(command[0]);
        } catch (erro) {
            console.log(erro);
        }
    } else {
        console.log("Use: node script.js <caminho_do_arquivo>");
    }
}
commandInline();

async function readFileByLine(file) {
    const fileStream = fs.createReadStream(file);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    rl.on("line", (line) => {
        const arrayValues = valueReset(line);
        console.log(validateValues(arrayValues));
    });
}

function valueReset(value) {
    return value.split("/");
}

function validateValues(value) {
    if (value.length === 1) return value[0];
    if (+value[0] === 0 || +value[1] === 0) return "ERR";
    return divisionValues(value);
}

function divisionValues(value) {
    const remainderDivision = value[0] % value[1] === 0;
    if (remainderDivision) {
        return value[0] / value[1];
    }
    const arraySort = [...value].sort();
    const maximumDivisor = maximumDivisorCommon(arraySort[0], arraySort[1]);
    const simplifyFraction = `${value[0] / maximumDivisor}/${value[1] / maximumDivisor}`;
    return maximumDivisor !== 1 ? simplifyFraction : calculateMixedFraction(value);
}

function maximumDivisorCommon(value1, value2) {
    const remainderDivision = value1 % value2;
    if (remainderDivision === 0) return value2;
    return maximumDivisorCommon(value2, remainderDivision);
}

function calculateMixedFraction(value) {
    const division = Math.floor(value[0] / value[1]);
    const remainderDivision = value[0] % value[1];
    if (division === 0) return `${value[0]}/${value[1]}`;
    return `${division} ${remainderDivision}/${value[1]}`;
}
