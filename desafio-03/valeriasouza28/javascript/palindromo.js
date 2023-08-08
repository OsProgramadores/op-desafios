function palindromeWithString(myString, str) {
    const newString = myString.toLowerCase().replace(/[^a-zA-Z0-9]/g, "");
    const stringReverse = newString.split("").reverse().join("");
    return newString === stringReverse ? stringReverse : false;
}

function generateNumbersInRange(start, end) {
    const numbers = [];
    const numbersPalindrome = [];

    for (let i = start; i <= end; i++) {
        numbers.push(i.toString());
    }

    for (let c = 0; c < numbers.length; c++) {
        const regex = /^\d{2,}$/
const regexTest = regex.test(numbers[c].toString())
if (regexTest) {
    const reverse = numbers[c].split("").reverse().join("");
        if (numbers[c] === reverse) {
            numbersPalindrome.push(numbers[c]);
        }
}
        
    }

    return numbersPalindrome;
}

let str = palindromeWithString("ama")
let num = generateNumbersInRange(1,20)
console.log(num);