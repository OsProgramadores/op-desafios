function palindromeNumbers(number){

    for (let x = 1; x < number; x++) {
        let numberConvert = x.toString().split('').reverse().join('');
        let numberReverse = parseInt(numberConvert);

        x === numberReverse ? console.log(x) : '';
    }
}

palindromeNumbers(10000);