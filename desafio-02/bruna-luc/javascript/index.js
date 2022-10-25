// Escreva um programa para listar todos os números primos entre 1 e 10000, na linguagem de sua preferência.

// 1passo :verrificar se o numero é primo

// 2passo : Armazenar os numeros no Array

// 3passo : Imprimir o array

const final = 10000
let count = 2
let count2 = 2
const primo = []

for (count; count < final; count++) {
  count2 = (count - 1)
  primo.push([count])
  for (count2; count2 > 1; count2--) {
    if ((count % (count2)) === 0) {
      count2 = 2
      if (count2 === 2) {
        primo.pop()
      }
    }
  }
}
console.log(`Números primos de 1 a 10000 ${primo}`)
