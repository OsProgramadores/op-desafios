function palindromes(start, end) {
    const numbers = [];
    const numbersPalindrome = [];
    for (let i = start; i <= end; i++) {
        numbers.push(i.toString());
    }

    for (let c = 0; c < numbers.length; c++) {
        const regex = /^\d{2,}$/;
        const regexTest = regex.test(numbers[c].toString());
        if (regexTest) {
            const reverse = numbers[c].split("").reverse().join("");
            if (numbers[c] === reverse) {
                numbersPalindrome.push(numbers[c]);
            }
        }
    }

    return numbersPalindrome;
}

const palindrome = palindromes(3000, 3010);
palindrome.forEach(element => {
    console.log(element);
});
