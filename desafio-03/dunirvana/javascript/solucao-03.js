(function(){
    console.log('Solucao Desafio 03 - imprimir todos os números palindrômicos entre dois outros números');

    testarPalindromo();

    /**
     * Realiza o teste com número definidos
     */
    function testarPalindromo() {
        var num1 = 1;
        var num2 = 200;

        for(let i = num1; i <= num2; i++) {
            ehPalindromo(i) ? console.log('Palindromo:', i) : null;
        }
    }

    /**
     * Verifica se um número é palindromo, comparando ele com ele mesmo invertido
     * @param num Numero a ser verificado
     */
    function ehPalindromo(num) {
        if (!num)
            return false;

        let numChar = String(num);
        return numChar === numChar.split('').reverse().join('');
    }

})();