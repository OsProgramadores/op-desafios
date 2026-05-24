const fs = require('fs');

function main(){

    function porDois(num){

        if(num == 0){
            return "false";
        }

        let nCont = 0;

        while(num % 2 == 0){

            num = num / 2;
            nCont++;

        }

        if(num == 1){
            return `true ${nCont}`;
        }else{
            return "false";
        }

    }

    const arquivo = './desafio-12/numeros.txt';

    const linhas = fs
        .readFileSync(arquivo, 'utf8')
        .split('\n');

    linhas.forEach(linha => {

        if(linha.trim() !== ''){

            const numero = Number(linha);

            console.log(porDois(numero));

        }

    });

}

main(); 