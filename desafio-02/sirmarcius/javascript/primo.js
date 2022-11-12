/* eslint-disable no-console */
/* eslint-disable no-use-before-define */
/* eslint-disable no-plusplus */
/*
Escreva um programa para listar todos os números primos
entre 1 e 10000.
*/

numerosPrimos(10000);

function numerosPrimos(limite) {
  for (let num = 2; num <= limite; num++) {
    if (verificarNumerosPrimos(num)) {
      console.log(num);
    }
  }
}
function verificarNumerosPrimos(numero) {
  for (let divisor = 2; divisor < numero; divisor++) {
    if (numero % divisor === 0) return false;
  }
  return true;
}
