function palind(num) {
  const palindromes = [];
  for (let i = 1; i <= num; i++) {
      const str = i.toString();
      const reversedStr = str.split("").reverse().join("");
      const reversedNum = parseInt(reversedStr);
      if (i === reversedNum) {
          palindromes.push(i);
      }
  }
  return palindromes;
}
console.log(palind(64));