numerosPrimos(10000)

function numerosPrimos(num) {
    for (var divisor = 2; divisor < num; divisor++) 
    if (num % divisor == 0) return false;
    return true;
}

var limitedeNumeros = 10000;

for (var i = 2; i < limitedeNumeros; i++) if (numerosPrimos(i)) console.log(i);

