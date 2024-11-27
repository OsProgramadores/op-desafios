let numerosPalidromos = [];
function palindromos(min, max) {
    for (; min <= max; min++) {
        const numInverso = min.toString().split("").reverse().join("");
        if (min == numInverso) {
            numerosPalidromos.push(min);
        }
    }
}
palindromos(1, 2000);
console.log(numerosPalidromos);
