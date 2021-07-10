function prime (max, arr = [2], n = 3, primo = true) {
  arr.map( i => n % i ? '' : primo = false )
  return n == max ? arr : prime(max, (primo ? arr.concat([n]) : arr), n + 1)
}
console.log(prime(10000))
