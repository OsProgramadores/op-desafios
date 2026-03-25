import { createReadStream } from 'fs'
import { createInterface } from 'readline'

function regex (fraction) {
  const regex = /[a-z]/i
  const test = regex.test(fraction)

  if (test === true) {
    return true
  } else {
    return false
  }
}

async function simplifyFraction (file) {
  const fileStream = createReadStream(file)

  const line = createInterface({
    input: fileStream,
    crlfDelay: Infinity
  })

  for await (const frac of line) {
    const isValid = regex(frac)

    if (isValid) {
      console.log('ERR')
      continue
    }

    let [numerator, denominator] = frac.split('/')

    numerator = parseInt(numerator)
    denominator = parseInt(denominator)

    if (numerator === 0 || denominator === 0) {
      console.log('ERR')
    } else if (!denominator) {
      console.log(`${numerator}`)
    } else if (isNaN(numerator) !== false || isNaN(denominator) !== false) {
      console.log('ERR')
    } else if (Number.isInteger(numerator) !== true || Number.isInteger(denominator) !== true) {
      console.log('ERR')
    } else if (numerator === denominator) {
      console.log('1')
    } else if (denominator === 1) {
      console.log(`${numerator}`)
    } else if (numerator < denominator) {
      if (denominator % numerator === 0) {
        console.log(`1/${denominator / numerator}`)
      } else {
        let half = Math.ceil(numerator / 2)

        for (half; half > 0; half--) {
          if (numerator % half === 0 && denominator % half === 0) {
            console.log(`${numerator / half}/${denominator / half}`)
            break
          }
        }
      }
    } else if (numerator > denominator) {
      let i = 0
      while (numerator > denominator) {
        numerator -= denominator
        i++
      }
      console.log(`${i} ${numerator}/${denominator}`)
    }
  }
}

const file = process.argv[2]

simplifyFraction(file)
