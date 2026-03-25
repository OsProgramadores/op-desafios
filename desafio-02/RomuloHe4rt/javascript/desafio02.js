(function () {
  console.log("Desafio 02 - Listar todos os números primos entre 1 e 10000.");

  exibirNumerosPrimos(10000);

  function exibirNumerosPrimos(limite) {
    for (let numero = 2; numero <= limite; numero++) {
      if (NumeroPrimo(numero)) console.log(numero);
    }
  }

  function NumeroPrimo(numero) {
    for (let divisor = 2; divisor < numero; divisor++) {
      if (numero % divisor === 0) {
        return false;
      }
    }
    return true;
  }
})();
