// Neste desafio, você deverá contabilizar e exibir a quantidade de cada peça em um tabuleiro de xadrez
// sem usar estruturas condicionais ou de múltipla escolha (sem *if*s, else e switch case).
const listOfPieces = [
    {name: "Peão",   code: 1},
    {name: "Bispo",  code: 2},
    {name: "Cavalo", code: 3},
    {name: "Torre",  code: 4},
    {name: "Rainha", code: 5},
    {name: "Rei",    code: 6}
];
const firstChessboard = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
];
const secondChessboard = [
    4, 3, 2, 5, 6, 2, 3, 4,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    4, 3, 2, 5, 6, 2, 3, 4
];
const getPiecesCount = (pieces, chessboard) => {
    return pieces.map( obj => {
        const piece = obj.name;
        const code = obj.code;
        const pieceCount = chessboard.filter( element => element === code).length;
        return `${piece}: ${pieceCount} peça(s)`;
    }).join("\n");
};
console.log(getPiecesCount(listOfPieces, firstChessboard));
console.log("\n");
console.log(getPiecesCount(listOfPieces, secondChessboard));