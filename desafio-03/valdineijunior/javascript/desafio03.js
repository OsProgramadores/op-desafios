function iterationBetweenNumbers(firstNumber, lastNumber) {
  if (
    typeof firstNumber !== 'number' ||
    typeof lastNumber !== 'number' ||
    firstNumber > lastNumber
  ) {
    console.log(
      'Os parâmetros devem ser dois números inteiros sendo o primeiro menor que o segundo.'
    )
  } else {
    for (let number = firstNumber; number <= lastNumber; number++) {
      if (checkIfTheNumberIsPalindrome(number)) {
        console.log(number)
      }
    }
  }
}

function checkIfTheNumberIsPalindrome(number) {
  let numberToCountDigit = number
  let numberOfDigits = 0
  while (numberToCountDigit >= 1) {
    numberToCountDigit /= 10
    numberOfDigits++
  }
  let expoente = 0
  let reverseNumber = 0
  while (numberOfDigits > 0) {
    const digit = Math.floor(
      (number % 10 ** numberOfDigits) / 10 ** (numberOfDigits - 1)
    )
    reverseNumber += digit * 10 ** expoente
    numberOfDigits--
    expoente++
  }
  if (number === reverseNumber) {
    return true
  } else {
    return false
  }
}

iterationBetweenNumbers(1, 10000)
