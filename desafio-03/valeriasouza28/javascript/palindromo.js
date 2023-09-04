const readline = require("readline-sync");
const numbers = [];
const palindromeNumbers = [];
const start = readline.question("Digite um número inicial: ");
const end = readline.question("Digite um número final: ");

for (let i = start; i <= end; i++) {
    numbers.push(i.toString());
}

for (let c = 0; c < numbers.length; c++) {
    const reverse = numbers[c].split("").reverse().join("");
    if (numbers[c] === reverse) {
        palindromeNumbers.push(numbers[c]);
    }
}

palindromeNumbers.forEach(element => {
    console.log(element);
});
