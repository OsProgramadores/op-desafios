let file_in = [
    [4,3,2,5,6,2,3,4],
    [1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [4,3,2,5,6,2,3,4]
];

let piece = {
    1: {
        nome: "Peão",
        quantidade: 0
    },
    2: {
        nome: "Bispo",
        quantidade: 0
    },
    3: {
        nome: "Cavalo",
        quantidade: 0
    },
    4: {
        nome: "Torre",
        quantidade: 0
    },
    5: {
        nome: "Rainha",
        quantidade: 0
    },
    6: {
        nome: "Rei",
        quantidade: 0
    }
}

file_in.forEach( (valor, chave) =>{
    valor.forEach( (valor, chave) =>{
        valor > 0 ? piece[valor].quantidade++ : null
    } )
} )

Object.entries(piece).forEach( (valor, chave) => {
    console.log(`${valor[1].nome}: ${valor[1].quantidade} peça(s)`)
} )