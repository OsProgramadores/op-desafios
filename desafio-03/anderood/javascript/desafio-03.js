function palindromeNumbers(number){

    for (let i = 0; i < 10; i++) {
        console.log(i)
    }

    for (let x = 10; x < number; x++) {
        let numberConvert = x.toString().split('').reverse().join('');
        let numberReverse = parseInt(numberConvert);

        x === numberReverse ? console.log(x) : '';
    }

}

palindromeNumbers(10000);