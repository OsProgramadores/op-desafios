var board = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]

var pieces = new Map();
for(let pieceCode = 0; pieceCode <= 6; pieceCode++){
    pieces.set(pieceCode, 0);
}

for(let x = 0; x < board.length; x++){
    for(let y = 0; y < board[x].length; y++){
        pieces.set(board[x][y], (pieces.get(board[x][y]) + 1));
    }
}

console.log(`Peão: ${pieces.get(1)} peça(s)\n`+
`Bispo: ${pieces.get(2)} peça(s)\n`+
`Cavalo: ${pieces.get(3)} peça(s)\n`+
`Torre: ${pieces.get(4)} peça(s)\n`+
`Rainha: ${pieces.get(5)} peça(s)\n`+
`Rei: ${pieces.get(6)} peça(s)\n`);
