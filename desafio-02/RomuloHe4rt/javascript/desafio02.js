(function () {
  console.log("Desafio 02 - Listar todos os números primos entre 1 e 10000.");

  for (let number = 1; number <= 10000; number++) {
    count = 0;

    for (let i = 1; i <= number; i++) {
      if (number % i === 0) {
        count++;
      };
    };

    if (count === 2) {
      console.log(number);
    };
  };
})();
