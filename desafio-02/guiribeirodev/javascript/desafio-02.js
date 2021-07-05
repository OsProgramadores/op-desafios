//Função "listaPrimo" é responsável por criar a lista dos números primos do número inicial até o numero final.
function listaPrimo(numeroInicio, numeroFim) {
  for (numeroInicio = 1; numeroInicio <= numeroFim; numeroInicio++) {
    verificaPrimo(numeroInicio, numeroFim)
  }
}

/* Função "verificaPrimo()"" irá verificar se o número é primo, a verificação é feita com base na premissa que todo número primo irá ter apenas dois divisores, o número 1 e ele próprio.*/
function verificaPrimo(numeroInicio) {
  let divisor = 0

  for (let count = 1; count <= numeroInicio / 2; count++) {
    if (numeroInicio % count == 0) {
      divisor++
    }

    if (divisor > 1) {
      break
    }
  }

  if (divisor == 1) {
    console.log(numeroInicio + ' é primo')
  }
}

listaPrimo(1, 10000)