(function(){
    console.log('Solucao Desafio 02 - listar todos os números primos entre 1 e 10000');

    realizarTestePrimos();

    /**
     * Dispara os testes
     */
    function realizarTestePrimos() {
        let ini = 1;
        let fim = 10000;

        for(var i = ini; i <= fim; i++) {
            ehPrimo(i) ? console.log(i) : null;
        }
    }

    /**
     * Verifica se o numero e primo
     * @param num Numero a ser checado
     */
    function ehPrimo(num) {
        if (num <= 1) 
            return false; // negativos

        if (num % 2 == 0 && num > 2) 
            return false; // pares

        let rq = Math.sqrt(num); // raiz quadrada para o limite das iteracoes, ja que ao menos um dos fatores deve ser menor ou igual a raiz
        for(let i = 3; i <= rq; i++) { // inicia em 3, encerra quando chegar na raiz quadrada, incrementa

            if(num % i === 0) 
                return false; // o modulo mostrara que um divisor foi encontrado
        }
        
        return true;
      }

})();