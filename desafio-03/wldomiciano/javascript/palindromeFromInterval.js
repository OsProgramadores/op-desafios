function isPalidrome(number) {
  if (number < 10) return true;
  const array = number.toString().split('');
  const reverse = array.reverse().join('');
  return number === Number(reverse);
}

function getPalidromeFromInterval(a, b) {
  const numbers = [];

  if (a < 0 || b < 0 || a > b) return numbers;

  for (let i = a; i <= b; i++) if (isPalidrome(i)) numbers.push(i);

  return numbers;
}

console.log(getPalidromeFromInterval(3003, 6010));
