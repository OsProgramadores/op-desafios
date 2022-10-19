listarNumerosPrimos(10000);

function listarNumerosPrimos(limite){
    for(let numero = 1; numero <= limite; numero++){

        if(NumeroPrimo(numero)) console.log(numero);

}



}

function NumeroPrimo(numero) {

    for (let divisor = 2; divisor < numero; divisor++){
          if(numero % divisor === 0) {

            return false;
          }

    }
     return true

}
