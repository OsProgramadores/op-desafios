export const ePalindromo = (n: string | number): boolean => {

  let s:string = '';

  if (typeof(n) === 'number') {
    s = n.toString();
  } else if (typeof(n) === 'string') {
    s = n;
  }

  if (s.indexOf('-') !== -1) {
    s = s.substring(1, s.length);
  }

  let i = 0;
  while (i < s.length) {
    if (s[i] !== s[(s.length - 1) - i]) {
      return false;
    }
    i++;
  }

  return true;
}