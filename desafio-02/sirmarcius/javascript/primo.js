/* Escreva um programa para listar todos os números primos
entre 1 e 10000. */

// eslint-disable-next-line require-jsdoc, consistent-return
function numeroPrimo(num) {
  // eslint-disable-next-line no-unreachable-loop, no-plusplus
  for (let divisor = 2; divisor < num; divisor++) {
    if (num % divisor === 0) {
      return false;
    }
    return true;
  }
}
const numero = 10000;
// eslint-disable-next-line no-plusplus
for (let i = 2; i < numero; i++) {
  // eslint-disable-next-line no-console
  if (numeroPrimo(i)) {
    // eslint-disable-next-line no-console
    console.log(i);
  }
}
