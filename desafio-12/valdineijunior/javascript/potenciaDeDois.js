const fs = require('fs')

const nome_arquivo = '/d12.txt'

const path = __dirname + `${nome_arquivo}`

function readFractions(path) {
  fs.readFile(path, 'utf-8', function (error, data) {
    if (error) {
      console.log('erro de leitura: ' + error.message)
    } else {
      const numbersArray = data.split('\r\n')
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
    }
  })
}
readFractions(path)
