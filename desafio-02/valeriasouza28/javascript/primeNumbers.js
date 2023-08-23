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
    const numbersPrimes = [];

    for (let i = start; i <= end; i++) {
        if (isPrime(i)) {
            numbersPrimes.push(i);
        }
    }

    return numbersPrimes;
}

const prime = generatePrimeInRange(1, 10000);

prime.forEach(element => {
    console.log(element);
});
