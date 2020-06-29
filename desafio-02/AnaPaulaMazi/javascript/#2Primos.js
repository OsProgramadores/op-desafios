function verificaPrimo(num){
let primo = true;
if(num<=1){ primo = false};
for(let i = 2; i < num; i++){ 

    if(num%i===0 && num!==i){
        primo = false;
        }  
   }       
   return primo;
}

let numeros = [];
for(let i = 0; i < 10000 ; i++){
 numeros[i] = i+1;
}

var ret = numeros.filter(verificaPrimo);

console.log(`Os numeros primos de 1 a 10000 são:\n ${ret}.`);