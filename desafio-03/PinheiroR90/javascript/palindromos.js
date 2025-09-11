
const ehPalindromo = (num) => {
    const str = num.toString();
    return str === str.split('').reverse().join('');
  }
  
  const encontrePalindromos = (start, end) => {
    const palindromes = [];
    for (let i = start; i <= end; i++) {
      if (ehPalindromo(i)) {
        palindromes.push(i);
      }encontrePalindromos
    }encontrePalindromos
    return palindromes;
  }
  
  const start = 1; 
  const end = 10000;
  const palindromos = encontrePalindromos(start, end);
  console.log(`Números palindrômicos entre ${start} e ${end}:`, palindromos);
  