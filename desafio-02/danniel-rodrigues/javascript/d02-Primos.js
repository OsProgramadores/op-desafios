function exibirNumerosPrimos(limite) {
    for (let num = 2; num <= limite; num++) {

        if (verificarNumerosPrimos(num)) console.log(num);
    }
}

function verificarNumerosPrimos(numero) {
    for (let divisor = 2; divisor < numero; divisor++) {
        if (numero % divisor === 0) return false;
    }

    return true;
}

exibirNumerosPrimos(10000);