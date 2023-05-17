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
        const reverse = numbers[c].split("").reverse().join("");
        if (numbers[c] === reverse) {
            numbersPalindrome.push(numbers[c]);
        }
    }

    return numbersPalindrome;
}

function isPalindrome(palindrome1, palindrome2) {
    if (typeof palindrome1 === "string" && typeof palindrome2 === "undefined") {
        const palindromeString = palindromeWithString(palindrome1);
        return palindromeString;
    } else if (
        typeof palindrome1 === "number" &&
        typeof palindrome2 === "number"
    ) {
        const palindromeNumber = generateNumbersInRange(
            palindrome1,
            palindrome2
        );
        return palindromeNumber;
    } else {
        console.log("Não é uma string nem um número");
    }
}

console.log(isPalindrome("ama"));
