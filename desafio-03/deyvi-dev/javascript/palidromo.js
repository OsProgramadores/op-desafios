function palindromo (number1, number2) {
  for (let i = number1; i <= number2; i++) {
    const validador = i.toString().split('').reverse().join('')
    if (parseInt(validador) === i) {
      console.log(i)
    }
  }
}
palindromo(1, 20)
palindromo(3000, 3010)
