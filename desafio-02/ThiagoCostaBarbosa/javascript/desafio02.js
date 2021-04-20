function primeNumbers(x) {
  let arr = []
  for (let n = 2; n <= x; n++) {
    count = 0
    for (let i = 2; i < n; i++) n % i ? '' : (count++, count > 0 ? i = n : '')
    count === 0 ? arr.push(n) : ''
  }
  return arr
}

console.log(primeNumbers(10000))