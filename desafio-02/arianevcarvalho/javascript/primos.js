function identifier(){
let primeNumbers=[],divisores = 0, l=0
for (let i = 2; i < 10000; i++){ 
    for (n=0; n<=i;n++){
        if (i%n==0){
           divisores+=1
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
console.log (identifier())