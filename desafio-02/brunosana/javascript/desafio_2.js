for (let i = 1; i<=10000;i++){
    let isPrimo = true;
    for (let j = 2; j<=parseInt(i/2) && isPrimo; j++)
        if ((i % j == 0) && (i!=j)) isPrimo = false;
    isPrimo ? console.log(i) : null
}