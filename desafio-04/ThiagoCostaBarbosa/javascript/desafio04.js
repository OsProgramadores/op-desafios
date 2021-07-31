function Chess_count(array) {
  let pieces = [0, "Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"],
      values = [0, 0, 0, 0, 0, 0, 0];

  //Remove Subarray
  array = array.flat();

  //Count number of pieces
  for (let i in array) {
    values[array[i]] += 1;
  }

  //Print the quantity of every piece
  console.log('\nQuantidade de peças:');
  for (i = 1; i < values.length; i++) {
    console.log(`${pieces[i]}: ${values[i]} peça(s)`);
  }
};

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

Chess_count(tabuleiro);
Chess_count(tabuleiro2);