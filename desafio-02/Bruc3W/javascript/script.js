const limite = 100

for (let i = 2; i <= limite; i++) {
  let ePrimo = true

  for (let divisor = 2; divisor < i; divisor++) {
    if (i % divisor === 0) {
      ePrimo = false
      break
    }
  }
  if (ePrimo) console.log(i)
}
