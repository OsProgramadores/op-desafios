//Função "listaPrimo" é responsável por criar a lista dos números primos do número inicial até o numero final.
function listaPrimo(numeroInicio, numeroFim) {
  for (numeroInicio = 1; numeroInicio <= numeroFim; numeroInicio++) {
    verificaPrimo(numeroInicio, numeroFim)
  }
}

/* Função "verificaPrimo()"" irá verificar se o número é primo, a verificação é feita 
com base na premissa que todo número primo irá ter apenas dois divisores, 
o número 1 e ele próprio, então caso o número de divisores sejam 2 será primo.*/
function verificaPrimo(numeroInicio, numeroFim) {
  let divisor = 0

  for (let count = 1; count <= numeroInicio; count++) {
    if (numeroInicio % count == 0) {
      divisor++
    }
    if (divisor > 2) {
      return divisor
    }
    if (numeroInicio <= numeroFim / 2) {
      return divisor
    }
  }

  if (divisor == 2) {
    console.log(numeroInicio + ' é primo')
  }
}

listaPrimo(1, 10000)
