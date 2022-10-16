function primos (num) {
  for (let n = 2; n < num; n++) {
    if (num % n === 0) return false
  }
  return true
}
const recebePrimos = (numeros) => {
  for (let contador = 2; contador < numeros; contador++) { if (primos(contador)) console.log(contador) }
}
recebePrimos(1000)
