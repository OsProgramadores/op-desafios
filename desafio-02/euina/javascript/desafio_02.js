/*
Escreva um programa para listar todos os números primos 
entre 1 e 10000, na linguagem de sua preferência.
*/

numerosPrimos(10000)

function numerosPrimos(num) {
    let numbers = new Array();
    for (var i = 0; i <= num; i++) {
      if (numPrimo(i)){
        numbers.push(i);
      }
    }
    return numbers;
  }
  function numPrimo(num) {
    for(let i = 2; i <num; i++)
      if(num % i === 0) {
          return false
      };
    return num >1;
    }
    
    console.log(numerosPrimos(10000));
    