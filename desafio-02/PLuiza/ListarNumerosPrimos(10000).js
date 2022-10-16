ListarNumerosPrimos(10000)

function ListarNumerosPrimos(limite){

    for(let numero = 1; numero <= limite; numero++){

    
        if (Primo(numero))console.log(numero);

    }

    }

    function Primo(numero) {

        let Primo = true;

        for (let divisor = 2; divisor < numero; divisor++){

            if(numero % divisor === 0){

            

            return false;
        }
    }

    return true;

    }