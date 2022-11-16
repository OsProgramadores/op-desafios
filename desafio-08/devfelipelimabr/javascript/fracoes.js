const fs = require('fs')
fs.readFile('src/frac.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  //Fraction simplification function
  function simplify(str) {
    var result = '', data = str.split('/'),
      numOne = Number(data[0]),
      numTwo = Number(data[1]);
    for (var i = Math.max(numOne, numTwo); i > 1; i--) {
      if ((numOne % i == 0) && (numTwo % i == 0)) {
        numOne /= i;
        numTwo /= i;
      }
    }
    if (numTwo === 1) {
      result = numOne.toString()
    } else {
      result = numOne.toString() + '/' + numTwo.toString()
    }
    return result
  }
  //Sorting and calculating fractions
  const fracoes = data.split('\n')

  let numerador = [];
  let denominador = [];
  let cociente = [];
  let resto = [];
  let result = [];

  for (let i = 0; i < fracoes.length; i++) {
    let numeradorDenominador = fracoes[i].split('/');
    numerador[i] = numeradorDenominador[0];
    denominador[i] = numeradorDenominador[1];
    cociente[i] = parseInt(numerador[i] / denominador[i]);
    resto[i] = numerador[i] % denominador[i];

    if (denominador[i] == 0) {
      result[i] = `ERR`;
    } else if (denominador[i] === undefined) {
      result[i] = `${numerador[i]}`;
    } else if (denominador[i] == 1) {
      result[i] = `${numerador[i]}`
    } else if (numerador[i] == denominador[i]) {
      result[i] = '1'
    } else if (cociente[i] == 0) {
      result[i] = simplify(resto[i] + '/' + denominador[i]);
    } else {
      result[i] = cociente[i] + ' ' + resto[i] + '/' + denominador[i];
    }
  }
  for (let i = 0; i < result.length; i++) {
    console.log((result[i]))
  }
});