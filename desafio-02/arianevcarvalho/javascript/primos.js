// Detectar números primos de 1 a 10000

/*Função para identificar os números primos*/

function identifier(){
    let primeNumbers=[],divisores = 0, l=0
    for (i=2; i<10000; i++){ 
        for (n=0; n<=i;n++){
            if (i%n==0){
                divisores +=1    
            }          
        }
        if (divisores<3){
            primeNumbers[l]=i
            l+=1
        }
         divisores=0
    }
   return primeNumbers
}


// Chamada da função

console.log (identifier())