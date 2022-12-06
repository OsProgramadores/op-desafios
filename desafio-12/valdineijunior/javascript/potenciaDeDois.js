let numbersArray = []
fetch('./d12.txt')
  .then(response => response.text())
  .then(text => {
    numbersArray = text.split('\n')
    numbersArray.pop()
    for (let i = 0; i < numbersArray.length; i++) {
      const element = numbersArray[i]
      let numberIsAPotentialOfTwo = false
      let expoent = 0n
      while ((2n ** expoent) <= element) {
        numberIsAPotentialOfTwo = (2n ** expoent) === BigInt(element)
        expoent++
      }
      if (numberIsAPotentialOfTwo) {
        expoent = expoent - 1n
        console.log(element, numberIsAPotentialOfTwo, parseInt(expoent))
      } else {
        console.log(element, numberIsAPotentialOfTwo)
      }
    }
  })
