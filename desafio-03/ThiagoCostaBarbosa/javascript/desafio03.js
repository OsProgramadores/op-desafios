function palindromos(max, min = 1, arr = []) {
  return min <= max ?
    min != [...(""+min)].reverse().join('') ?
      palindromos(max, min + 1, arr) :
      palindromos(max, min + 1, arr.concat([min])) :
    arr
}
console.log(palindromos(3010, 3000))
