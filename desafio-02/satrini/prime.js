/*
  Challenge of: OsProgramadores.com
  Problem: List all prime numbers between 1 and 10000
  Github: https://github.com/satrini
  Language: JavaScript
*/

let prime = (limit) => {
  let total = 0;
  let c = 0;
  
  for (let num = 2; num <= limit; num++) {
    for (let i = 1; i <= num; i++) {
      if (num % i === 0) {
        c++;
      }
    }
    
    if (c == 2) {
      console.log(`${num} is prime!`);
      total++;
    }
    
    c = 0;
  }
  
  return total;
}

result = prime(10000);
console.log('Total prime numbers:', result);


