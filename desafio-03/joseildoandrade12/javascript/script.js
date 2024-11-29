function palindromos(min, max) {
    const valueMin = min;
    const valueMax = max;
    const numerosPalidromos = [];
    for (; min <= max; min++) {
        const numInverso = +min.toString().split("").reverse().join("");
        if (min === numInverso) {
            numerosPalidromos.push(min);
        }
    }
    console.log(
        `os números palindromos entre ${valueMin} e ${valueMax} são : ${numerosPalidromos}`
    );
    return numerosPalidromos;
}

function verificacao(value) {
    if (isNaN(value)) {
        console.log("Coloque apenas valores númericos");
    } else if (value < 1) {
        console.log("Adicione apenas valores positivos ou maior que 0");
    } else if (!Number.isInteger(value)) {
        console.log("Adicione apenas números inteiros");
    } else {
        return true;
    }
}

const readline = require("node:readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Informe o valor minimo: ", (min) => {
    if (!verificacao(+min)) {
        rl.close();
    } else {
        rl.question("Informe o valor máximo: ", (max) => {
            if (!verificacao(+max)) {
                rl.close();
            } else if (min >= max) {
                console.log(
                    "O valor mínimo não pode ser maior ou igual ao valor máximo"
                );
            } else {
                palindromos(+min, +max);
            }
            rl.close();
        });
    }
});
