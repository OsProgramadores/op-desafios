const numbers = [];
for (let i = 1; i <= 100; i++) {
    numbers.push(i);
}

const palindromicos = numbers.filter((num) => {
    const original = num;
    let reversed = 0;

    while (num > 0) {
        const digit = num % 10;
        reversed = reversed * 10 + digit;
        num = Math.floor(num / 10);
    }

    return original === reversed;
});
console.log(palindromicos);


