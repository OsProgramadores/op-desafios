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
        if (Number(numbers[i]) !== 1) {
            if (powOfTwo(numbers[i]) > 0) {
                console.log(numbers[i] + " " + "true" + " " + powOfTwo(numbers[i]));
            } else {
                console.log(numbers[i] + " " + "false" + " " + powOfTwo(numbers[i]));
            }
        } else {
            console.log(numbers[i] + " " + "true" + " " + 0);
        }
    }
}

function powOfTwo(num) {
    let power = 1;
    let result = 0;
    if (Number(num) === 0) {
        return result;
    }
    while (num % 2 === 0) {
        num = num / 2;
        power++;
        if (num === 2) {
            result = power;
        }
    }
    return result;
}
