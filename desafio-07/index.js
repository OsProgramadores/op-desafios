function main(){

    const linhas = [];

    const fs = require('fs');
                    
    const file = './desafio-07/palavras.txt';

    const rl = require('readline').createInterface({
        input: fs.createReadStream(file)
    });

    rl.on('line', (line) => {
        linhas.push(line);
    });

    rl.on('close', () => {

        for(let i = linhas.length - 1; i >= 0; i--){
            console.log(linhas[i]);
        }

    });

}

// comando certo;
// node .\desafio-07\index.js .\desafio-07\teste.txt
main();