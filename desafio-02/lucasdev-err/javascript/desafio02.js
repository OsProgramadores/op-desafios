function primeNumbers(num) {
    const numbers = [];
    for (let i = 0; i <= num; i++){
        if (isPrime(i)) {
            numbers.push(i);
        }
    }
    return numbers;
}
function isPrime(num) {
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return num > 1;
}
console.log(primeNumbers(10000));
