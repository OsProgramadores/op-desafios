
pecas = {
    1: {peca: "Peão", quantidade: 0},
    2: {peca: "Bispo", quantidade: 0},
    3: {peca: "Cavalo", quantidade: 0},
    4: {peca: "Torre", quantidade: 0},
    5: {peca: "Rainha", quantidade: 0},
    6: {peca: "Rei", quantidade: 0}
}

tabuleiro1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]

]

tabuleiro2 = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]


function contarPecas( tabuleiro){

        let quant = 0;

        for (const x in pecas) {
            pecas[x].quantidade = 0;            
        }         

    tabuleiro.forEach( (valor, chave) => {
        valor.forEach((valor, chave) => {
           quant =  valor > 0 ? pecas[valor].quantidade++ : null;
            return quant;
        });
        
    });
}

function imprimir (ret){
    for (const x in pecas) {
        console.log (`${pecas[x].peca}: ${pecas[x].quantidade} peça(s)`);
        
    }
}

console.log('Resultado do primerio tabuleiro:')
let ret1 = contarPecas(tabuleiro1);
 imprimir (ret1);
 console.log('\n');
 console.log('Resultado do segundo tabuleiro:')
let ret2 = contarPecas(tabuleiro2);
imprimir (ret2);