const readline = require("readline-sync");
const numbers = [];
const start = readline.question("Digite um número inicial: ");
const end = readline.question("Digite um número final: ");

for (let i = start; i <= end; i++) {
    numbers.push(i.toString());
}

numbers.forEach(element => {
    const reverse = element.split("").reverse().join("");
    if (element === reverse) {
        console.log(element);
    }
});
