let tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

let tabuleiro2 = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]

//All the code below on one line would be this:
//let a = [tabuleiro, tabuleiro2].forEach(function (array) {let r = [array, [0,0,0,0,0,0], ["Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"], ["peça", "peças"], "Quantidade de peças:\n"], v = [r[0].flat().map(i => r[1][i-1] += 1), r[1].map((v,i) => r[4] += ["",`${r[2][i]}: ${v} ${r[3][(v != 1) * 1]}\n`][(v != 0) * 1]), console.log(r[4])] });

Chess_count(tabuleiro)
Chess_count(tabuleiro2)

function Chess_count(array) {
        //r[0] All pieces in Chess table
let r = [array,
        //r[1]Quantity of Pieces
        [0, 0, 0, 0, 0, 0],
        //r[2] Types of pieces
        ["Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"],
        //r[3]Noun
        ["peça", "peças"],
        //r[4] Result
        "Quantidade de peças:\n"],
        //Remove Subarrays
    v = [r[0].flat()
            //Count quantity of every piece
            .map(i => r[1][i - 1] += 1),
        //Loop to assemble the quantity phrase in the result
        r[1].map((v, i) => r[4] += ["",
                                    //Piece
                                    `${r[2][i]
                                    //Quantity
                                    }: ${v
                                    //Noun - is singular ou plural
                                    } ${r[3][(v != 1) * 1]
                                    //Condictional without a conditional function - only add to result if a type have piece
                                    }\n`][(v != 0) * 1]),
        //Print result
        console.log(r[4])]
}
