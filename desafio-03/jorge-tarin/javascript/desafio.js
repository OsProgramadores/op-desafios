function validaPalindromo(num) {
    const auxNum = num.toString();
    const revNum = auxNum.split("").reverse().join("");

    if (auxNum === revNum) {
        console.log(num);
    }
}

function exibePalindromos(min, max) {
    // valida os parâmetros
    if (isNaN(min) || isNaN(max)) {
        console.log("Erro: ambos os parâmetros precisam ser números.");
        return;
    } else if (min > max) {
        const aux = max;
        max = min;
        min = aux;
    }

    for (let i = min; i <= max; i++) {
        validaPalindromo(i);
    }
}

const min = Number(process.argv[2]);
const max = Number(process.argv[3]);

exibePalindromos(min, max);
