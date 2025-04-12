
const numbers = [];
for (let i = 1; i <= 10000; i++) {
    numbers.push(i);
};

const cousinNumber = numbers.filter((num) => {
    if (num > 1) {
        let count = 0;
        for (let i = 1; i <= num; i++) {
            if (num % i === 0) {
                count++;
            }
        }
        return count === 2;
    }
    return false;
});

console.log(cousinNumber); 
