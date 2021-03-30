listNumbers = []

isPrime = (number) => {
    if (number < 2) { return false }
    if (number % 2 == 0 && number > 2) { return false }

    for (let i = 3; i <= Math.sqrt(number); i++) {
        if (number % i === 0) { return false }
    }
    return true
}

for (let i = 0; i < 10000; i++) {
    listNumbers.push(i)
}

console.log(listNumbers.filter(isPrime))
