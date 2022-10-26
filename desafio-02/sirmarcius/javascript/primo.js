/* Escreva um programa para listar todos os números primos
entre 1 e 10000.*/

// eslint-disable-next-line require-jsdoc
function numeroPrimo(num) {
    for (let divisor = 2; divisor < num; divisor++) {
    if (num % divisor === 0) {
    return false;
    }
  return true;
}
const numero = 10000;
for (let i = 2; i < numero; i++)
 if (numeroPrimo(i)) console.log(i);