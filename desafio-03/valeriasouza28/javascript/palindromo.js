const numbers = [];
const numbersPalindrome = [];

function palindrome(start, end) {
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

const usingPalindrome = palindrome(1, 20);

usingPalindrome.forEach(element => {
    console.log(element);
});
