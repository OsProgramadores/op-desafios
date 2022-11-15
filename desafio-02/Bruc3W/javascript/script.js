var limite = 100;

for(i = 2; i <= limite; i++){
    let ePrimo = true

    for (divisor = 2; divisor < i; divisor++){
        if(i % divisor === 0){
            ePrimo = false;
            break;
        }
    }
    if(ePrimo) console.log(i);
}