const readline = require("readline-sync");

const start = readline.question("Digite um número: ");
const end = readline.question("Digite um número: ");
const numbers = [];
const numbersPalindrome = [];

for (let i = start; i <= end; i++) {
    numbers.push(i.toString());
}

for (let c = 0; c < numbers.length; c++) {
    const reverse = numbers[c].split("").reverse().join("");
    if (numbers[c] === reverse) {
        numbersPalindrome.push(numbers[c]);
    }
}

numbersPalindrome.forEach(element => {
    console.log(element);
});
