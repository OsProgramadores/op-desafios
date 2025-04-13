const numbers = [];
for (let i = 1; i <= 10000; i++) {
    numbers.push(i);
};

const cousinNumber = numbers.filter((num) => {
    if (num < 2) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
});
console.log(cousinNumber);
