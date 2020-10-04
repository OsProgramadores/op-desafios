//A função abaixo irá receber um tabuleiro de Xadrez cujo números de casas é determinado pelo usuário,
//onde, normalmente, conta com 64 casas (8 x 8).


function matriz (col, lin) {
    //A variável Matriz é a escolhida para receber os dados das colunas e linhas do tabuleiro
    let matriz = [];
    let i = 0;
    let j = 0;
    //Utilizando Nested For Loops - ou For Loops dentro de outors - vamos criar arrays que serão os números
    //de linhas e enviá-los para a Matriz, lembrando que cada vez que rodarmos o For loop para as linhas,
    //o loop entenderá que deve-se criar novamente um array linha vazio []
    for(i = 0; i < lin; i++){
      let linha = [];
      matriz.push(linha);
      for(j = 0; j < col; j++){
        //Já aqui, a variável coluna irá gerar aleatoriamente números entre 0 e 6
        //Para isso, usamos a função Math.floor que serve para arredondar os números
        //E a função Math.random que gera números aleatórios entre 0 e 1.
        //Multiplicamos por 7 para que os resultados sejam arredondados para 0 - o menor
        //E 6 - o maior
        let coluna = Math.floor((Math.random() * 7));
        matriz[i].push(coluna);
      }
      }
      //Aqui visualizamos como nosso tabuleiro está até então
    console.log(matriz);
      //para que seja feita a contagem de peças, criamos a variável pecas, sendo essa
      //um array vazio que irá receber o valor inicial 0 através do For Loop.
      //O usuário pode também declarar as variáveis por si só, caso queira
    let pecas = [];
    for (i = 0; i < 8; i++){
      pecas.push(0);
    }
    //Aqui utilizamos novamente Nested Loops para checarmos os valores de cada linha e coluna
    //Como os valores podem ir de 0 até 6 - em concordância com os valores do array pecas acima
    //Cada vez que o for loop retornar um valor, ele vai acrescentar 1 ao valor correspondente
    //do índice da variável pecas
    for (i = 0; i < matriz.length; i++){
      for (j = 0; j < matriz[i].length; j++){
        pecas[matriz[i][j]]++;
      }
    }
    //com isso, criamos variaveis representando as possibilidades de pecas
    //Associadas a um determinado indice no array. Por conta do For Loop acima
    //cada variável já tem um valor armazenado, será utilizado abaixo
    vazio = pecas[0];
    peao = pecas[1];
    bispo = pecas[2];
    cavalo = pecas[3];
    torre = pecas[4];
    rainha = pecas[5];
    rei = pecas[6];
    //Por fim, iremos retornar os valores das peças abaixo.
    console.log("Casas vazias: " + vazio);
    console.log("Peões: " + peao);
    console.log("Bispos: " + bispo);
    console.log("Cavalos: " + cavalo);
    console.log("Torres: " + torre);
    console.log("Rainhas: " + rainha);
    console.log("Reis: " + rei);
  }
  matriz(8, 8);