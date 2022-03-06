const readline = require('readline')
const rl = readline.createInterface(process.stdin, process.stdout)

let board = [[], [], [], [], [], [], [], []]
let count = 0

const clearScreen = () => {
  console.log('\033[0m\033[2J\033c')
}

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
    4: "[Enter] pra continuar ou [c] para contar as peças: \r"
  }

  return questObj[q]
}

const pieces = "\n1-Peão 2-Bispo 3-Cavalo 4-Torre 5-Rainha 6-Rei\n"

const updateBoard = () => {
  clearScreen()
  console.table(board)
  console.log(`${pieces}
    \rInsira o numero da peça na posição desejada\n`)
}

const showCount = () => {
  let flatBoard = board.flat()
  let countPieces = countOccurr(flatBoard)

  clearScreen()
  console.table(board)
  console.log(`${pieces}
    \rPeão: ${countPieces(1)} peça (s)
    \rBispo: ${countPieces(2)} peça (s)
    \rCavalo: ${countPieces(3)} peça (s)
    \rTorre: ${countPieces(4)} peça (s)
    \rRainha: ${countPieces(5)} peça (s)
    \rRei: ${countPieces(6)} peça (s)
    \r\n[Enter] para continuar ou [ctrl + d] pra finalizar`)
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
    } else {
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
