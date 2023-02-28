function palind(num) {
  const palindrome = [];
  for (let i = 1; i <= num; i++) {
      const str = i.toString();
      const reversedStr = str.split("").reverse().join("");
      const reversedNum = parseInt(reversedStr);
      if (i === reversedNum) {
          palindrome.push(i);
      }
  }
  return palindrome;
}
console.log(palind(64));