const goal = 10000;
const primes = [2];
console.time();

function isPrime(n) {
  if (!(n % 2)) return false;
  const square = Math.sqrt(n);
  for (let i = 2; i <= square; i++) if (!(n % i)) return false;
  return true;
}

for (let n = 3; n <= goal; n++) if (isPrime(n)) primes.push(n);

console.log(`Total de números primos encontrados: ${primes.length}`);
console.timeEnd();
