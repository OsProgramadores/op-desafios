import { ePrimo } from './e-primo';

(function main () {

  const max = 10000;
  let i = 0;
  
  const primos = [];
  
  while (i < max) {
    if (ePrimo(i)) {
      primos.push(i);
    }
    i++;
  }
  
  console.log(primos);

})();
