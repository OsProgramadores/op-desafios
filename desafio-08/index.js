const fs = require('fs');

function mdc(a, b){

    while(b != 0){
        let temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

function simplificar(linha){

    linha = linha.trim();

    // número inteiro
    if(!linha.includes('/')){
        return linha;
    }

    let [num, den] = linha.split('/').map(Number);

    // erro divisão por zero
    if(den === 0){
        return "ERR";
    }

    let divisor = mdc(num, den);

    num = num / divisor;
    den = den / divisor;

    // virou inteiro
    if(den === 1){
        return `${num}`;
    }

    // fração imprópria vira número misto
    if(num > den){
        let inteiro = Math.floor(num / den);
        let resto = num % den;
        return `${inteiro} ${resto}/${den}`;
    }

    return `${num}/${den}`;
}

function main(){

    const arquivo = './desafio-08/frac.txt';

    const linhas = fs
        .readFileSync(arquivo, 'utf8')
        .split('\n');

    linhas.forEach(linha => {
        if(linha.trim() !== ''){
            console.log(simplificar(linha));
        }
    });

}

main();