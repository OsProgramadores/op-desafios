export const ePrimo = (n:number): boolean => {

  if (n < 2) {
    return false;
  }

  let i:number = n - 1;
  while( i > 1 ) {
    if (n % i === 0) {
      return false;
    }
    i--;
  }

  return true;
}
