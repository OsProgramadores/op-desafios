//Aqui está uma função que irá determinar os números palíndromos entre um intervalo de números comprimidos
//entre o primeiro número (x) e o segundo número (y)
function isPalyndrome(x, y) {
  //Antes de qualquer coisa, vamos checar a condição para o programa rodar independente de x ser maior ou menor que y, e vice-versa
  if (x < y) {
    //Após checada a condição, o for loop se encarregará de processar os números na ordem correta
    for (i = x; i <= y; i++) {
      
      //Aqui a mágica acontece. A variável reverse irá se encarregar de ler o valor de i,
      //transformá-lo em uma String usando o toString(),
      //desmembrar o valor da array com o split(), para algarismos com dois ou mais dígitos,
      //inverter a ordem do array com utilizando o reverse() e,
      //por fim, combinar o valor do array com a ordem invertida em um novo número com join()
      //Para termos certeza que o resultado é um número, utilizamos a função Number()
      //que irá passar no teste de equalidade utilizando '==='
      var reverse = Number(i.toString().split([]).reverse().join([]));

      //Checando mais uma condição, caso a variável reverse seja igual ao número i
      //O programa irá exibir o número, e irá repetir o processo até checar todos os
      //números no intervalo definido pelo usuário
      if (reverse === i) {
        console.log(i);
      }
    }

    //O código abaixo é a outra condição caso o número x seja maior que y, exibindo assim
    //os números na ordem descrescente
  } else {
    for (i = x; i >= y; i--) {
      var reverse = Number(i.toString().split([]).reverse().join([]));
      if (reverse === i) {
        console.log(i);
      }
    }
  }
}

isPalyndrome(100, 1);
