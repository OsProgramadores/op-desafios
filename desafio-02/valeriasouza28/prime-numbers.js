// Código para verificar se um número é primo ou não

const final = 10
function generatePrime() {
  for (let i = 0; i <= final; i++) {
    if (i === 1) {} 
    else if (i === 2) {
      console.log(i + 'É um número primo!')
    } else if (i % 2 === 0) {} 
    else {
      console.log(i + 'É um número primo!')
    }
  }
}
generatePrime()
