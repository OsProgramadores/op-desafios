// Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números.
const isValidNumber = (min, max) => (Number.isInteger(min) && Number.isInteger(max))
    && (Math.sign(min) === 1 ? true : false && Math.sign(max) === 1 ? true : false)
    && min <= max;
const reverseNumber = number => parseInt(String(number).split("").reverse().join(""));
const getPalindromicNumbers = (min, max) => {
    const range = (max - min) + 1;
    return !isValidNumber(min, max)
        ?   "Insira números válidos, inteiros e positivos, número inicial menor ou igual ao número final."
        :   Array(range).fill(null).map((_, index) => min + index)
                .filter( number => reverseNumber(number) === number ? number : null);
};
console.log(getPalindromicNumbers(1, 20));
console.log(getPalindromicNumbers(3000, 3003));