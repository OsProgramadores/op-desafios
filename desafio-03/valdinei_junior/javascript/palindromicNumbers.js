function palindromicNumbers (firstNumber, lastNumber) {
  if (typeof firstNumber !== 'number' || typeof lastNumber !== 'number' || firstNumber > lastNumber) {
    console.log('Os parâmetros dever ser dois números inteiros sendo o primeiro menor que o segundo.')
  } else {
    for (let number = firstNumber; number <= lastNumber; number++) {
      let lengthNumber = number.toString().length
      let expoente = 0
      let reverseNumber = 0
      while (lengthNumber > 0) {
        const digit = Math.floor(
          ((number % 10 ** lengthNumber) / 10 ** (lengthNumber - 1))
        )
        reverseNumber += (digit * 10 ** expoente)
        lengthNumber--
        expoente++
      }
      if (number === reverseNumber) {
        console.log(number)
      }
    }
  }
}

palindromicNumbers(1, 10000)
