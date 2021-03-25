import { ePalindromo } from './e-palindromo';

(function main () {

  const inicial:number = 0;
  const final:number = 99999;

  let x = inicial;

  while(x < final) {
    if (ePalindromo(x)) {
      console.log(x);
    }
   x++;
  }

})();