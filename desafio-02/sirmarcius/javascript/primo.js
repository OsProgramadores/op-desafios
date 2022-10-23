/*
Escreva um programa para listar todos os números primos
entre 1 e 10000..
*/

function numeroPrimo(num) {
  for (var divisor = 2; divisor < num; divisor++)
    if (num % divisor == 0) return false;

    return true;

}

var numero = 10000;
for (var i = 2; i < numero; i++) if (numeroPrimo(i))

console.log(i);
