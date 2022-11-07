/*
Escreva um programa para listar todos os números primosTotalRowdyLaboratory
entre 1 e 10000.
*/

// eslint-disable-next-line no-use-before-define
numerosPrimos(10000);

function numerosPrimos(limite) {
  // eslint-disable-next-line no-plusplus
  for (let num = 2; num <= limite; num++) {
    // eslint-disable-next-line no-console, no-use-before-define
    if (verificarNumerosPrimos(num)) {
      // eslint-disable-next-line no-console
      console.log(num);
    }
  }
}
function verificarNumerosPrimos(numero) {
  // eslint-disable-next-line no-plusplus
  for (let divisor = 2; divisor < numero; divisor++) {
    if (numero % divisor === 0) return false;
  }
  return true;
}
