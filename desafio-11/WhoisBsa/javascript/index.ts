// Primes in pi - WhoisBsa
import fs from 'fs';

const data = fs.readFileSync('./data.txt', 'utf8');
const numbers = data.slice(2);
const primeList = new Set<number>();

let primeSequence = '';
let maxSequence = '';
let currentSequence = '';
let currentNumber = '';
let numberIndex = 0;

const minPrime = 2;
const maxPrime = 9973;
const isPrimeNumber = (number: number) => {
  if (number < 2 || (number % 2 == 0 && number > 2)) return false;

  const s = Math.sqrt(number);
  for (let i = 3; i <= s; i += 2)
    if (number % i === 0) return false;

  primeList.add(number);
};

isPrimeNumber(minPrime);
for (let i = minPrime - 1; i <= maxPrime; i += 2)
  isPrimeNumber(i);

for (let i = 1; i < numbers.length; i++) {
  if (primeSequence.length > numbers.length - i) break;

  while (numberIndex < numbers.length)
    getPrimeSequence(numberIndex, 5);

  if (maxSequence.length > primeSequence.length)
    primeSequence = maxSequence;

  maxSequence = '';
  numberIndex = i;
}

function getPrimeSequence(currentPosition: number, slice: number): void {
  if (slice === 0) {
    if (!currentSequence) {
      numberIndex = numbers.length;
      return;
    }

    return addToSequence();
  }

  currentNumber = numbers.slice(currentPosition, currentPosition + slice);

  if (primeList.has(+currentNumber)) {
    currentSequence = currentNumber;

    if (currentNumber.length === 2)
      return addToSequence();
  }
  getPrimeSequence(currentPosition, slice - 1);
}

function addToSequence(): void {
  numberIndex += currentSequence.length;
  maxSequence += currentSequence;
  currentSequence = '';
}

console.log({ primeSequence });
