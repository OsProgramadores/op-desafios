function palindromeNumbers(number){

    let numbers = [];

    for (let i = 0; i < 10; i++) {
        numbers.push(i)
    }

    for (let x = 10; x < number; x++) {
        let numberConvert = x.toString().split('').reverse().join('');
        let numberReverse = parseInt(numberConvert);
        x === numberReverse ? numbers.push(x) : '';
    }

    return numbers;
}

const result = palindromeNumbers(100);

console.log(result);