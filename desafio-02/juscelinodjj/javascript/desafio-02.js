// Escreva um programa para listar todos os números primos entre 1 e 10000
const getPrimeNumbers = range => {
    return (isNaN(range) || range < 2)
        ?   "Insira um número válido, sendo ele maior ou igual a dois"
        :   Array(parseInt(range)).fill(null).map((_, index) => ++index)
                .filter( number => {
                    const dividers = Array(number).fill(null).map((_, index) => ++index);
                    const dividersForThisNumber = dividers.filter( divider => number % divider === 0);
                    return dividersForThisNumber.length === 2 ? number : null;
                });
};
console.log(getPrimeNumbers(10000));