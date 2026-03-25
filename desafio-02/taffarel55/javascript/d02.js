const max = 10000;
const min = 1;

const isPrimeNumber = (num) => {
  if (num < 2) return false;
  for (let div = 2; div * div <= num; div++) {
    if (num % div === 0) return false;
  }
  return true;
};

for (let num = min; num < max; num++) {
  if (isPrimeNumber(num)) {
    console.log(num);
  }
}
