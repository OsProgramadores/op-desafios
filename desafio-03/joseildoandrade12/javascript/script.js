const numerosPalidromos = [];
function palindromos(min, max) {
    if (min < 1 || max < 1) {
        console.log("Adicione apenas valores positivos ou maior que 0");
    } else if (min >= max) {
        console.log(
            "O valor mínimo não pode ser maior ou igual ao valor máximo"
        );
    } else if (!(Number.isInteger(min) && Number.isInteger(max))) {
        console.log("Adicione apenas números inteiros");
    } else {
        for (; min <= max; min++) {
            const numInverso = +min.toString().split("").reverse().join("");
            if (min === numInverso) {
                numerosPalidromos.push(min);
            }
        }
    }
}
palindromos(1, 100);
console.log(numerosPalidromos);