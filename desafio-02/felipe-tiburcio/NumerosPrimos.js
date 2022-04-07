function app() {
  let primes = [];

  for (let i = 1; i <= 10000; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }
  console.log(primes);
}

function isPrime(n) {
  let isPrime = false;
  let divisions = [];

  for (let i = 1; i < n; i++) {
    if (n % i === 0) {
      divisions.push(n / i);
    }
  }

  if (divisions.length === 1) {
    isPrime = true;
  }

  return isPrime;
}

app();
