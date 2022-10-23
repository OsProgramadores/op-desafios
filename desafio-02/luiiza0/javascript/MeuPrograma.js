listarNumerosPrimos(10000)
function listarNumerosPrimos(limite) {
  for (var numero = 2; numero <= limite; numero++) {
    if (numeroPrimo(numero)) console.log(numero)
  }
}
function numeroPrimo(numero) {
  for (var divisor = 2; divisor < numero; divisor++) {
    if (numero % divisor === 0) {
      return false
    }
  }
  return true
}
