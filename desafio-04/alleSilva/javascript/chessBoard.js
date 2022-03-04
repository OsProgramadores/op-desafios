const readline = require('readline')
const rl = readline.createInterface(process.stdin, process.stdout)

let board = [[], [], [], [], [], [], [], []]
let pieceInput = 0
let lineInput = -1
let columnInput = -1
let count = 0

for(let i = 0; i <= 7; i++){
  for(let j = 0; j <= 7; j++){
    board[i][j] = 0;
  }
}

const countOccurr = (arr, val) => arr.reduce((a, v) => (v === val ? a + 1 : a), 0)

const fillPosition = (piece) => (line) => (column) => {
  board[line][column] = parseInt(piece)
}

function quest (q) {
  if (q == 1) {return "Digite o número da peça (1-6): "}
  if (q == 2) {return "Digite a posição da linha (0-7): "}
  if (q == 3) {return "Digite a posição da coluna (0-7): "}
  if (q == 4) {
    return "Enter pra continuar ou c para contar as peças \r"}
}
var fp = fillPosition

function getInput() {
  updateBoard()
  count++
  if (count ==1) {fp = fillPosition}
  rl.question(quest(count), x => {
    fp = fp(x)
    getInput()
    if (x == 'c') {
      show()
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

function updateBoard(){
  console.log('\033[2J')
  console.table(board)
  console.log('\r')
  console.log("Insira o numero da peça na posição desejada")
  console.log('\r')
  options()
}

function options () {
  console.log("1-Peão", "2-Bispo", "3-Cavalo", "4-Torre", "5-Rainha", "6-Rei")
  console.log('\r')
}

function show(){
  updateBoard()
  flatBoard = board.flat()
  console.log("Peão:", countOccurr(flatBoard, 1), "peça (s)")
  console.log("Bispo:", countOccurr(flatBoard, 2), "peça (s)")
  console.log("Cavalo:", countOccurr(flatBoard, 3), "peça (s)")
  console.log("Torre:", countOccurr(flatBoard, 4), "peça (s)")
  console.log("Rainha:", countOccurr(flatBoard, 5), "peça (s)")
  console.log("Rei:", countOccurr(flatBoard, 6), "peça (s)")

}

getInput()
