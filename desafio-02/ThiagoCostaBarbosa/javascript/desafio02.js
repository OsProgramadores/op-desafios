function primeNumbers(x) {
  parseInt(x)
  var arr = [2]
  for (let n = 3; n <= x; n++) {
    count = 0
    arr.map(a => n % a ? '' : count++)
    count === 0 ? arr.push(n) : ''
  }
  return arr
}

// Alternativa um pouco mais funcional
function prime2(max, arr = [2], n = 3) {
  parseInt(max)
  let p = arr.map(i => n % i ? true : false).includes(false)
  return n == max ? arr : prime2(max, (p ? arr : arr.concat([n])), n + 1)
}