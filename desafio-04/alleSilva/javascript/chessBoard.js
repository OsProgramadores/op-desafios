const readline = require('readline')
const rl = readline.createInterface(process.stdin, process.stdout)

let board = [[], [], [], [], [], [], [], []]
let count = 0

const fillBoardWithZero = () => {
  for(let i = 0; i <= 7; i++){
    for(let j = 0; j <= 7; j++){
      board[i][j] = 0;
    }
  }
}

const countOccurr = (arr) => (val) => arr.filter(el => el == val).length

const fillPosition = (piece) => (line) => (column) => {
  board[line][column] = parseInt(piece)
}

let fp = fillPosition

const quest = (q) => {
  questObj = {
    1: "Digite o número da peça (1-6): ",
    2: "Digite a posição da linha (0-7): ",
    3: "Digite a posição da coluna (0-7): ",
    4: "Enter pra continuar ou c para contar as peças: \r"
  }

  return questObj[q]
}

const pieces = "1-Peão 2-Bispo 3-Cavalo 4-Torre 5-Rainha 6-Rei"

const updateBoard = () => {
  console.log('\033[2J')
  console.table(board)
  console.log('\r')
  console.log("Insira o numero da peça na posição desejada")
  console.log('\r')
  console.log(pieces)
  console.log('\r')
}

const showCount = () => {
  let flatBoard = board.flat()
  let countPieces = countOccurr(flatBoard)

  console.log('\033[2J')
  console.log(pieces)
  console.log('\r')
  console.table(board)
  console.log('\r')
  console.log(`Peão: ${countPieces(1)} peça (s)`)
  console.log(`Bispo: ${countPieces(2)} peça (s)`)
  console.log(`Cavalo: ${countPieces(3)} peça (s)`)
  console.log(`Torre: ${countPieces(4)} peça (s)`)
  console.log(`Rainha: ${countPieces(5)} peça (s)`)
  console.log(`Rei: ${countPieces(6)} peça (s)`)
  console.log('\r')
  console.log("Enter para continuar ou ctrl + d pra finalizar")
}

const getInput = () => {
  updateBoard()
  count++
  if (count == 1) {
    fp = fillPosition
  }
  rl.question(quest(count), x => {
    if ((count == 1 && (x < 0 || x > 6)) || ((count == 2 || count == 3) && x < 0 || x > 7)){
      count--
      updateBoard()
    } else
    {
      fp = fp(x)
    }
    getInput()
    if (x == 'c' || x == 'C') {
      showCount()
      count = 0
    }

    rl.resume()

    if (count == 4) {
      count = -1
      fp = fillPosition
      updateBoard()
      getInput()
    }
  })
}

fillBoardWithZero()
getInput()
