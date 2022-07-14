const { readFileSync } = require('fs')
const file = process.argv[2]
const input = readFileSync(file, 'utf-8')


let values = input.split('\n').filter((value) => {
  return value
})

function isPotency(number) {
  /* A função é feita usando BigInt, pois a divisão com  números maiores que o MAX_SAFE_INTEGER
  sempre resultam em infinity.*/
  number = BigInt(number)
  let exponent = 0

  while (number >= 1n) {
    if (number == 1n) {
      return ['true', exponent]
    }
    else if (number % 2n != 0n) {
      return ['false', exponent]
    }
    number /= 2n
    exponent += 1
  }

  return ['false', exponent]
}

function main() {
  for (value of values) {
    const result = isPotency(value)
    if (result[0] == "true") {
      console.log(value, result[0], result[1])
    }
    else {
      console.log(value, result[0])
    }
  }
}

main()