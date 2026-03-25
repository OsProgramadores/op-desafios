//Percorre o número inicial ao final verificando se é palíndromo
function palindromesList(initialNumber, finalNumber) {
  for (initialNumber; initialNumber <= finalNumber; initialNumber++) {
    isPalindrome(initialNumber);
  }
}

//Verifica se o número é um palíndromo
function isPalindrome(numberToRate) {
  var number = numberToRate.toString().substr(0);
  var numberBackward = number.split('').reverse().join('');

  if (number == numberBackward) {
    console.log(`O número ${numberToRate} é Palíndromo`);
  }
}

palindromesList(3000, 8008);
