const fs = require('fs');

// gera todos os primos até 9973
function gerarPrimos(){

    const limite = 9973;

    const sieve = Array(limite + 1).fill(true);

    sieve[0] = false;
    sieve[1] = false;

    for(let i = 2; i * i <= limite; i++){

        if(sieve[i]){

            for(let j = i * i; j <= limite; j += i){
                sieve[j] = false;
            }

        }

    }

    const primos = new Set();

    for(let i = 2; i <= limite; i++){

        if(sieve[i]){
            primos.add(String(i));
        }

    }

    return primos;
}

function main(){

    // lê o arquivo pi.txt
    const pi = fs
        .readFileSync(__dirname + '/pi.txt', 'utf8')
        .replace(/\D/g, '');

    const primos = gerarPrimos();

    const memo = {};

    function buscar(index){

        if(index >= pi.length){
            return '';
        }

        if(memo[index] !== undefined){
            return memo[index];
        }

        let melhor = '';

        // tenta 1, 2, 3 e 4 dígitos
        for(let tam = 1; tam <= 4; tam++){

            const parte = pi.slice(index, index + tam);

            if(primos.has(parte)){

                const resto = buscar(index + tam);

                const atual = parte + resto;

                if(atual.length > melhor.length){
                    melhor = atual;
                }

            }

        }

        memo[index] = melhor;

        return melhor;
    }

    let resposta = '';
    let maior = 0;

    for(let i = 0; i < pi.length; i++){

        const seq = buscar(i);

        if(seq.length > maior){

            maior = seq.length;
            resposta = seq;

        }

    }

    console.log(resposta);

}

main();