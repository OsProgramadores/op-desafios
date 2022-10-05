for (var i = 1; i <= 100000; i++) {
  var ehPalidromo = true

  var string = String(i).split('')

  for (var j = 0; j < string.length / 2; j++) {
    if (string[j] != string[string.length - (1 + j)]) {
      ehPalidromo = false
      break
    }
  }

  if (ehPalidromo) {
    console.log(i)
  }
}
