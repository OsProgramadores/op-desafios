import { ePrimo } from './../e-primo';

test('Testar com numeros primos como entrada', () => {

  expect(ePrimo(2)).toBeTruthy();
  expect(ePrimo(3)).toBeTruthy();
  expect(ePrimo(5)).toBeTruthy();
  expect(ePrimo(7)).toBeTruthy();
  expect(ePrimo(11)).toBeTruthy();
  expect(ePrimo(13)).toBeTruthy();
  expect(ePrimo(17)).toBeTruthy();
  expect(ePrimo(19)).toBeTruthy();
  expect(ePrimo(23)).toBeTruthy();
  expect(ePrimo(29)).toBeTruthy();

});


test('Testar com numeros não primos como entrada', () => {

  expect(ePrimo(0)).toBeFalsy();
  expect(ePrimo(-1)).toBeFalsy();
  expect(ePrimo(1)).toBeFalsy();
  expect(ePrimo(4)).toBeFalsy();
  expect(ePrimo(6)).toBeFalsy();
  expect(ePrimo(8)).toBeFalsy();
  expect(ePrimo(9)).toBeFalsy();
  expect(ePrimo(10)).toBeFalsy();
  expect(ePrimo(12)).toBeFalsy();
  expect(ePrimo(14)).toBeFalsy();
  expect(ePrimo(32)).toBeFalsy();

});