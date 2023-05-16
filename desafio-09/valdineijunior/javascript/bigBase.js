const base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const file = process.argv[2];
if (!file) {
    console.log('Você precisa fornecer um arquivo como argumento, utilize o arquivo teste "baseconv.txt"');
    process.exit(1);
}
const readline = require("readline");
const fs = require("fs");

const myInterface = readline.createInterface({
    input: fs.createReadStream(file)
});

myInterface.on("line", function (line) {
    return console.log(readBigBase(line));
});

function readBigBase(element) {
    const numbers = element.split(" ").splice(0, 3);
    const inputBase = numbers[0];
    const outputBase = numbers[1];
    const entryNumber = numbers[2];
    const response = checksIfTheInputIsValid(inputBase, outputBase, entryNumber);
    if (response === "valid") {
        const numberInBaseTen = convertToDecimal(inputBase, entryNumber);
        return convertDecimalToBaseOutput(outputBase, numberInBaseTen);
    } else return response;
}

function checksIfTheInputIsValid(inputBase, outputBase, entryNumber) {
    const maxBase = 62;
    const minBase = 2;
    const invalidBases =
        inputBase < minBase || inputBase > maxBase || outputBase < minBase || outputBase > maxBase;
    const negativeNumber = parseInt(entryNumber) < 0;
    let InvalidNumberForInputBase = false;
    const ValidDigitsForInputBase = [...base.slice(0, inputBase)];
    for (let index = 0; index < entryNumber.length; index++) {
        const element = entryNumber[index];
        const digitBelongsToBase = ValidDigitsForInputBase.includes(element);
        if (!digitBelongsToBase) {
            InvalidNumberForInputBase = true;
            break;
        }
    }
    if (invalidBases || negativeNumber || InvalidNumberForInputBase) {
        return "???";
    }
    const numberInBaseTen = convertToDecimal(inputBase, entryNumber);
    const limit = BigInt(
        convertToDecimal(maxBase, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    );
    if (numberInBaseTen > limit) {
        return "???";
    }
    if (numberInBaseTen === 0n) {
        return entryNumber;
    }
    return "valid";
}

function convertDecimalToBaseOutput(outputBase, numberInBaseTen) {
    let result = "";
    while (numberInBaseTen > 0) {
        const remainder = numberInBaseTen % BigInt(outputBase);
        result = base[remainder] + result;
        numberInBaseTen = (numberInBaseTen - remainder) / BigInt(outputBase);
    }
    return result;
}

function convertToDecimal(inputBase, entryNumber) {
    const arrayBase = base.split("");
    let numberInBaseTen = 0n;
    let exponent = BigInt(entryNumber.length - 1);
    for (let index = 0; index < entryNumber.length; index++) {
        const element = entryNumber[index];
        let exponentiatedBase = 1n;
        for (let j = 0; j < exponent; j++) {
            exponentiatedBase *= BigInt(inputBase);
        }
        const elementInBaseTen = BigInt(
            arrayBase.findIndex((char) => char === element)
        );
        numberInBaseTen += elementInBaseTen * exponentiatedBase;
        exponent--;
    }
    return numberInBaseTen;
}
