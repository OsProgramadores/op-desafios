function numerosPrimos(numero) {
    const listaNumerosPrimos = [];
    for (let numeroAtual = 1; numeroAtual <= numero; numeroAtual += 1){
        let numeroPrimo = true;
        for (let numeroDivisor = 2; numeroDivisor <= numeroAtual; numeroDivisor += 1){
            if (numeroAtual % numeroDivisor === 0 && numeroAtual !== numeroDivisor){
                numeroPrimo = false;
                break;
            }
        }
        if (numeroPrimo === true && numeroAtual !== 1){
            listaNumerosPrimos.push(numeroAtual);
        }
    }
    return listaNumerosPrimos;
}

console.log(numerosPrimos(1000));