const fs = require('fs')

function readFractions(path) {
  fs.readFile(path, 'utf-8', function (error, data) {
    if (error) {
      console.log('erro de leitura: ' + error.message)
    } else {
      const fractions = data.split('\r\n')
      fractions.pop()
      for (let index = 0; index < fractions.length; index++) {
        const element = fractions[index]
        const fintDivisor = (/(\/)\w/)
        const ElementIsAlreadyAninteger = !fintDivisor.test(element)
        if (ElementIsAlreadyAninteger) {
          console.log(element)
        } else {
          const ArrayWithNumeratorAndDenominator = element.split('/')
          const numerator = parseInt(ArrayWithNumeratorAndDenominator[0])
          const denominator = parseInt(ArrayWithNumeratorAndDenominator[1])
          const denominatorIsZero = denominator === 0
          if (denominatorIsZero) {
            console.log('ERR')
          } else {
            const quotient = numerator / denominator
            const resresultOfDivisionIsAninteger = Number.isInteger(quotient)
            if (resresultOfDivisionIsAninteger) {
              console.log(quotient.toString())
            } else {
              if (numerator > denominator) {
                const remainder = numerator % denominator
                const simplifiedNumerator = numerator - remainder
                const integer = simplifiedNumerator / denominator
                console.log(`${integer} ${remainder}/${denominator}`)
              } else {
                const proportion = denominator / numerator
                const theTwoNumbersaremultiples = Number.isInteger(proportion)
                if (theTwoNumbersaremultiples) {
                  const canBeSimplified = numerator > 1
                  if (canBeSimplified) {
                    const simplifiedNumerator = numerator / proportion
                    const simplifiedDenominator = denominator / proportion
                    console.log(`${simplifiedNumerator}/${simplifiedDenominator}`)
                  } else {
                    console.log(`${numerator}/${denominator}`)
                  }
                } else {
                  for (let index = numerator; index > 0; index--) {
                    const checkNumerador = Number.isInteger(numerator / index)
                    const checkDenominador = Number.isInteger(denominator / index)
                    if (checkNumerador && checkDenominador) {
                      const simplifiedNumerator = numerator / index
                      const simplifiedDenominator = denominator / index
                      console.log(`${simplifiedNumerator}/${simplifiedDenominator}`)
                      break
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  })
}
readFractions('./frac.txt')
