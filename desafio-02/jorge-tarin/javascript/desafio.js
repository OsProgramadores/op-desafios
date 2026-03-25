function validaPrimo(num) {
    if (num <= 1) {
        return false;
    }
    for (let i = 2; i < Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

for (let i = 1; i < 10000; i++) {
    if (validaPrimo(i)) {
        console.log(i);
    }
}
