function main() {
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

  let types = [
    [1, "Peão"],
    [2, "Bispo"],
    [3, "Cavalo"],
    [4, "Torre"],
    [5, "Rainha"],
    [6, "Rei"]]

  let nomenclatura = ["peça", "peças"]

  let arr1 = concat_subarray(tabuleiro)
  types.map(el => console.log(`${el[1]}: ${count_in_array(arr1, el[0])} ${print_singvsplur(count_in_array(arr1, el[0]), nomenclatura)}`))

  let arr2 = concat_subarray(tabuleiro2)
  types.map(el => console.log(`${el[1]}: ${count_in_array(arr2, el[0])} ${print_singvsplur(count_in_array(arr2, el[0]), nomenclatura)}`))
}

function concat_subarray(arr) {
  return arr.reduce((acc, curr) => acc.concat(curr), [])
}

function count_in_array(arr, num) {
  return arr.filter((value) => value === num).length
}

function print_singvsplur(num, arr) {
  return arr[(num != 1) * 1]
}
