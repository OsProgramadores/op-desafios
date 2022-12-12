/*
Exibir os números primos de 1 até 10000.
*/

exibirPrimos(10000);

function exibirPrimos(total) {
  for (let num = 2; num <= total; num++) {
    if (verificarPrimos(num)) console.log(num);
  }
}

function verificarPrimos(numero) {
  for (let divisor = 2; divisor < numero; divisor++) {
    if (numero % divisor === 0) return false;
  }

  return true;
}
