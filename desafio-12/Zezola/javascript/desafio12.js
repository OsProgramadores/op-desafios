const fs = require("fs");
fs.readFile("./d12.txt", "utf8", (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    const splittedData = data.split("\n");
    splittedData.pop();
    solve(splittedData);
});

function solve(numbers) {
    for (let i = 0; i < numbers.length; i++) {
        const numberBigInt = BigInt(numbers[i]);
        if (numberBigInt !== 1n) {
            if (powOfTwo(numberBigInt) > 0n) {
                console.log(numbers[i] + " " + true + " " + powOfTwo(numbers[i]));
            } else {
                console.log(numbers[i] + " " + false);
            }
        } else {
            console.log(numbers[i] + " " + true + " " + 0);
        }
    }
}

function powOfTwo(num) {
    let numBigInt = BigInt(num);
    let power = 1;
    let result = 0;
    if (numBigInt === 0n) {
        return result;
    }
    while (numBigInt % 2n === 0n) {
        numBigInt = numBigInt / 2n;
        power++;
        if (numBigInt === 2n) {
            result = power;
        }
    }
    return result;
}
