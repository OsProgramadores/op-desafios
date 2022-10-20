const file = process.argv[2]
const readline = require('readline')
const fs = require('fs')

const myInterface = readline.createInterface({
  input: fs.createReadStream(file)
})

myInterface.on('line', function (line) {
  return validaPotencia(line)
})
function validaPotencia (v) {
  const result = v
  const convert = BigInt(v)
  v = convert
  const f = v && !(v & (v - 1n))
  if (f) {
    const n = v.toString(2).length - 1
    return console.log(v <= 0n ? 0n : result + ' true' + ' ' + BigInt(n))
  } else {
    console.log(result + ' false')
  }
}
