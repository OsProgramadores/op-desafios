function testPalindromes(n) {
  nPal = parseInt(n.toString().split('').reverse().join(''))
  if (n === nPal) {
    return true
  } else {
    return false
  }
}

function listPalindromes(min, max) {
  console.time('Tempo de execução')

  if (isNaN(min) || isNaN(max)) {
    console.log('Erro: ambos os parâmetros precisam ser números.')
    return
  } else if (min > max) {
    let temp = min
    min = max
    max = temp
  }

  count = 0
  for (let n = min; n <= max; n++) {
    if (testPalindromes(n)) {
      console.log(n)
      count++
    }
  }

  switch (count) {
    case 0:
      console.log(`Não existem palíndromos entre ${min} e ${max}`)
      break
    case 1:
      console.log(`Existe 1 palíndromo entre ${min} e ${max}`)
      break
    default:
      console.log(`Existem ${count} palíndromos entre ${min} e ${max}.`)
  }

  console.timeEnd(`Tempo de execução`)
}

console.log(
  `Esse programa lista os palíndromos numéricos entre dois inteiros positivos:`
)

let min = Number(process.argv[2]);
let max = Number(process.argv[3]);

listPalindromes(min, max)

if (process.argv[4] != undefined) {
  console.log(`Obs.: Apenas os dois primeiros números foram considerados.`);}