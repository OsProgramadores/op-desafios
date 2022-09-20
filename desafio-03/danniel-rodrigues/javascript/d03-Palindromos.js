function definirPalindromo(numInicial, numFinal) {
    let palindromos = [];
    
    while (numInicial <= numFinal) {
        let intLength = ('' + numInicial).length;

        if (intLength == 1) {
            palindromos.push(numInicial);
        }
        else {
            let str = numInicial.toString();
            let inverso = str.split("").reverse().join("");
            
            if(str == inverso) {
                palindromos.push(numInicial);
            }
        }

        numInicial++;
    }

    return palindromos;
}

function exibirPalindromos(numInicial, numFinal) {
    let numPalindromos = definirPalindromo(numInicial, numFinal);
    
    console.log(`Palindromos de ${numInicial} a ${numFinal} são: ${numPalindromos.toString()}`);

}

exibirPalindromos(1, 20);