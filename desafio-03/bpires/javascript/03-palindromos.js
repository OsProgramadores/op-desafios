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
    console.log('Error: both parameters must be numbers')
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
      console.log(`Existem ${count} palíndromos entre ${min} e ${max}`)
  }

  console.timeEnd(`Tempo de execução`)
}

const prompt = require('prompt-sync')()

console.log(
  `This program lists the numeric palindromes between two positive integers.`
)

let min = Number(prompt(`Please provide the first number: `))
let max = Number(prompt(`Please provide the second number: `))

listPalindromes(min, max)
