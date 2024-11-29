const numerosPalidromos = [];
function palindromos(min, max) {
    for (; min <= max; min++) {
        const numInverso = +min.toString().split("").reverse().join("");
        if (min === numInverso) {
            numerosPalidromos.push(min);
        }
    }
    return numerosPalidromos;
}

function verificacao(min, max) {
    if (typeof min !== "number" || typeof max !== "number") {
        console.log("Coloque apenas valores númericos");
    } else if (min < 1 || max < 1) {
        console.log("Adicione apenas valores positivos ou maior que 0");
    } else if (min >= max) {
        console.log(
            "O valor mínimo não pode ser maior ou igual ao valor máximo"
        );
    } else if (!(Number.isInteger(min) && Number.isInteger(max))) {
        console.log("Adicione apenas números inteiros");
        return;
    } else {
        palindromos(min, max);
    }
}
console.log(verificacao(1, 50));
console.log(numerosPalidromos);
