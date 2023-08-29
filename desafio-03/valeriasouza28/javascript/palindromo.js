const numbers = [];
const numbersPalindrome = [];

function prime(start, end) {
    for (let i = start; i <= end; i++) {
        numbers.push(i.toString());
    }

    for (let c = 0; c < numbers.length; c++) {
        const reverse = numbers[c].split("").reverse().join("");
        if (numbers[c] === reverse) {
            numbersPalindrome.push(numbers[c]);
        }
    }
    return numbersPalindrome;
}

const usingPrime = prime(1, 20);

usingPrime.forEach(element => {
    console.log(element);
});
