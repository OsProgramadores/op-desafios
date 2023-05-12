function isPrime(num) {
    if (num === 1) {
        return false;
    } else if (num === 2) {
        return true;
    } else if (num % 2 === 0) {
        return false;
    } else {
        for (let i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i === 0) {
                return false;
            }
        }
        return true;
    }
}

function generatePrimeInRange(start, end) {
    const numbers = [];
    const numbersPrimes = [];

    for (let i = start; i <= end; i++) {
        numbers.push(i);
    }
    for (let c = 0; c < numbers.length; c++) {
        const prime = isPrime(numbers[c]);
        if (prime === true) {
            numbersPrimes.push(numbers[c]);
        }
    }
    return numbersPrimes;
}
console.log(generatePrimeInRange(1, 10000));
