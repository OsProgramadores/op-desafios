const tabuleiro1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

const tabuleiro2 = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]

function main(){

    const tabuleiro = tabuleiro2;

    let peao = 0;
    let bispo = 0;
    let cavalo = 0;
    let torre = 0;
    let rainha = 0;
    let rei = 0;

    for(let i = 0; i < tabuleiro.length; i++){

        for(let j = 0; j < tabuleiro[i].length; j++){

            const valor = tabuleiro[i][j];

            if(valor == 1){
                peao++;
            }
            else if(valor == 2){
                bispo++;
            }
            else if(valor == 3){
                cavalo++;
            }
            else if(valor == 4){
                torre++;
            }
            else if(valor == 5){
                rainha++;
            }
            else if(valor == 6){
                rei++;
            }
        }
    }
    console.log(`Peão: ${peao} peça(s)`);
    console.log(`Bispo: ${bispo} peça(s)`);
    console.log(`Cavalo: ${cavalo} peça(s)`);
    console.log(`Torre: ${torre} peça(s)`);
    console.log(`Rainha: ${rainha} peça(s)`);
    console.log(`Rei: ${rei} peça(s)`);
}

main();