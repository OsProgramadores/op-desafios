let input = [
  [4, 3, 2, 5, 6, 2, 3, 4],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [4, 3, 2, 5, 6, 2, 3, 4]
];

let input2 = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
];

function countChessPieces(board) {
  let countPieces = [0, 0, 0, 0, 0, 0, 0];

  //Contabiliza a quantidade de peças de acordo com índice da matriz
  for (x = 0; x < board.length; x++) {
    for (y = 0; y < board.length; y++) {
      countPieces[board[x][y]]++;
    }
  }

  var pieces = {
    1: {
      name: 'Peão',
      amount: countPieces[1]
    },
    2: {
      name: 'Bispo',
      amount: countPieces[2]
    },
    3: {
      name: 'Cavalo',
      amount: countPieces[3]
    },
    4: {
      name: 'Torre',
      amount: countPieces[4]
    },
    5: {
      name: 'Rainha',
      amount: countPieces[5]
    },
    6: {
      name: 'Rei',
      amount: countPieces[6]
    }
  };

  //Imprime a saída
  for (i = 1; i <= 6; i++) {
    console.log(`${pieces[i].name}: ${pieces[i].amount} peça(s)`);
  }
}

countChessPieces(input2);
