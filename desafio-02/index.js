function main(){

    const inicio = 1;
    const fim = 1000;

    for(let contador = inicio; contador <= fim; contador++){
        if (ehPrimo(contador)){
            console.log(`${contador} é primo.  `);
            console.log('');
        }
    }

    function ehPrimo(numero){
        if(numero < 2){
            return false;
        }
        for(let i = 2; i < numero; i++){
            if(numero % i == 0){
                return false;
            }
        }
        return true;
    }

}

main();