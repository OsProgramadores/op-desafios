function main(){

    const fs = require('fs');

    const entrada = process.argv[2];

    if(!entrada){
        console.log("Digite uma frase.");
        process.exit();
    }

    const frase = entrada.toUpperCase();

    if(!/^[A-Z ]+$/.test(frase)){
        console.log("Erro");
        process.exit();
    }

    const limpa = frase.replace(/ /g, '');

    // lê words.txt
    const palavras = fs
        .readFileSync(__dirname + '/words.txt', 'utf8')
        .split('\n')
        .map(p => p.trim().toUpperCase());

    function contarLetras(texto){

        const contador = {};

        for(let letra of texto){
            contador[letra] = (contador[letra] || 0) + 1;
        }

        return contador;
    }

    function podeUsar(base, palavra){

        const letras = contarLetras(palavra);

        for(let letra in letras){

            if(!base[letra]){
                return false;
            }

            if(letras[letra] > base[letra]){
                return false;
            }

        }

        return true;
    }

    function remover(base, palavra){

        const novo = {...base};

        for(let letra of palavra){
            novo[letra]--;
        }

        return novo;
    }

    function vazio(obj){

        for(let letra in obj){

            if(obj[letra] > 0){
                return false;
            }

        }

        return true;
    }

    const base = contarLetras(limpa);

    // filtra palavras possíveis
    const palavrasValidas = palavras.filter(p =>
        podeUsar(base, p)
    );

    function resolver(restantes, usadas){

        if(vazio(restantes)){

            console.log(
                usadas.sort().join(' ')
            );

            return;
        }

        palavrasValidas.forEach(palavra => {

            if(podeUsar(restantes, palavra)){

                resolver(
                    remover(restantes, palavra),
                    [...usadas, palavra]
                );

            }

        });

    }

    resolver(base, []);

}
// para rodar é
// node desafio-06\index.js (palavra); 
main();