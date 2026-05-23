function main(){

    const inicio = 200;
    const fim = 304;

    for(let contador = inicio; contador <= fim; contador++){

        if (ehPalindromo(contador)){
            console.log(`${contador} é palindromo.  `);
            console.log('');
        }
    }

    function ehPalindromo(n){
        const texto = String(n);
        const invertido = texto.split('').reverse().join('');
        return texto == invertido;
    }

}

main();