/* OsProgramadores.com

Desafio #2: Listando números primos 

Instruções: Escreva um programa para listar todos os números primos entre 1 e 10000, na linguagem de sua preferência. */

let primeNumbers = []

function testPrimo(n) {
  if (n <= 1) {
    return false
  }

  for (let d = 2; d < n; d++) {
    if (n % d == 0) {
      return false
    }
  }

  return true
}

function primeNumbersList(a, b) {
  for (let n = a; n <= b; n++) {
    if (testPrimo(n)) {
      primeNumbers.push(n)
    }
  }

  let result

  switch (primeNumbers.length) {
    case 0:
      result = `Não existem números primos entre ${a} e ${b}.`
      break
    case 1:
      result = `Existe um número primo entre ${a} e ${b}, sendo este o número ${primeNumbers}.`
      break
    default:
      result = `Existem ${primeNumbers.length} números primos entre ${a} e ${b}, listados a seguir: \n ${primeNumbers}.`
  }

  console.log(result)
}

primeNumbersList(1, 1000)

// Para fins do exercício, considerou-se que o enunciado descreve um intervalo fechado, ou seja, números entre 1 e 1000, incluindo ambos os extremos.
