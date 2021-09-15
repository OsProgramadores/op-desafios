//Programa que lista todos números primos entre 1 e 10000 

//Array com os primeiros números primos da lista
let primos = [2, 3, 5, 7, 11]

//Imprime os primeiros números primos da lista
for (let c in primos) {
  console.log(primos[c])
}

//Insere os números entre 2 a 10000 a serem verificados na função
for (let i = 2; i < 10000; i++) {
  verificadorPrimo(i)
}


//Função que verifica se os números são primos
function verificadorPrimo(num) {

  //Loop que descarta se o número não for primo e imprime se for
  for (let pos in primos) { 
    //Caso o número inserido tenha resto igual a 0 com algum número primo, ele é descartado
    if (num % primos[pos] == 0) {
      break
      //Se o número não for divisível por nenhum número primo, ele é imprimido e colocado no array
    } else if (pos == primos.length - 1) {
        console.log(num)
        primos.push(num)
     }
  }
}