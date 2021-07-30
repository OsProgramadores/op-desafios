
function Chess_count(array) {

  pieces = ["Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"]
  values = [0, 0, 0, 0, 0, 0, 0]
  
  //Remove Subarray
  array = array.flat();

  //Count number of pieces
  for (element in array) {
    values[array[element]] += 1;
  }
  //Remove empty values
  values.shift()

  //Print the quantity of every piece
  console.log('\nQuantidade de peças:')
  for (let element in values) {
    console.log(`${pieces[element]}: ${values[element]} peça(s)`)
  }
}

let tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]]

let tabuleiro2 = [
  [4, 3, 2, 5, 6, 2, 3, 4],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [4, 3, 2, 5, 6, 2, 3, 4]]

Chess_count(tabuleiro)
Chess_count(tabuleiro2)
