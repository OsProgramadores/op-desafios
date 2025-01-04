// Criar um algoritmo que me retore todos números primos ate 10.000

// Criar uma função que faz um loop que armazena as informações em uma array

function primeNumbers(num){
    let numbers = new Array()

    for (let i = 0; i <= num; i++){
        if (isPrime(i)){
            numbers.push(i)
        }
    }

    return numbers
}

// Criar uma verificação se o número é primo ou não (utilizando um loop)

function isPrime(num){
    for (var i = 2; i < num; i++){
        if(num % i === 0){
            return false
        }
    }
    return num > 1
}

console.log(primeNumbers(10000))