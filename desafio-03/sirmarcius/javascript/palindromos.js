/*
Desafio-03: Verificar números palindromos.
*/

palindrome(100000);

function palindrome(number) {
    for (let index = 1; index < number; index++) {
        const numberConvert = index.toString().split("").reverse().join("");
        const numberReverse = parseInt(numberConvert);
        if (index === numberReverse) { console.log(index); }
    }
}
