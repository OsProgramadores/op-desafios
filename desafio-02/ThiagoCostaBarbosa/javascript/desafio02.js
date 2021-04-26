function prime(max) {
  if (parseInt(max) && max > 1) {
    parseInt(max)
  } else {
    arr = []
    n = 1
    max = 1
  }
  var arr = [2]
  for (let n = 3; n <= max; n++) {
    count = 0
    arr.map(i => n % i ? '' : count++)
    count === 0 ? arr.push(n) : ''
  }
  return arr
}

// Alternativa um pouco mais funcional
function prime2(max, arr = [2], n = 3) {
  (parseInt(max) && max > 1) || (arr = [], n = 1, max = 1)
  return n == max ? arr : prime2(max, (arr.map(i => n % i ? true : false).includes(false) ? arr : arr.concat([n])), n + 1)
}