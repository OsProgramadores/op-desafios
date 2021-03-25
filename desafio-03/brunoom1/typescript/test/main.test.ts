import { ePalindromo } from './../e-palindromo';

describe('Teste com numero palindromicos', () => {

  const numbers = [];

  let i = -9; 
  while (i < 10) {
    numbers.push(i++);
  }

  numbers.push(11);
  numbers.push(101);
  numbers.push(2002);
  numbers.push(23432);
  numbers.push(-131);
  numbers.push('123456780000090000087654321');
  
  i = 0;
  while(i < numbers.length) {
    test(`test number ${numbers[i]}`, () => {
      expect(ePalindromo(numbers[i])).toBeTruthy();
    });
    i++;
  }

});

describe('Teste com numeros não palindromicos', () => {

  const numbers = [];

  numbers.push(12);
  numbers.push(134351);
  numbers.push(20012);
  numbers.push(234232);
  numbers.push('131311');
  numbers.push('1234567800004090000087654321');
  
  let i = 0;
  while(i < numbers.length) {
    const value = numbers[i++];
    test(`test número ${value}`, () => {
      expect(ePalindromo(value)).toBeFalsy();
    });
  }

});