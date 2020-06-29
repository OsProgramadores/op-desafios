
function verificaPrimo(num){
let cont = 0;
for(let i = 0; i < num; i++){
   if((num%(i+1)) === 0){
       cont += 1;
   }  
}

if(cont === 2){
    return true;
    }
}

let numeros = [];
for(let i = 0; i < 10000 ; i++){
 numeros[i] = i+1;
}

var ret = numeros.filter(verificaPrimo);

console.log(`Os numeros primos de 1 a 10000 são:\n ${ret}.`);