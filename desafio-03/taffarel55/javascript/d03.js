const reverseNumberWithMethods = (n) =>
  Number(n.toString().split("").reverse().join(""));

const reverseNumber = (n) => {
  let r = "";
  while (n > 0) {
    r += n % 10;
    n = parseInt(n / 10);
  }
  return Number(r);
};

const runPerformanceTest = (...arguments) => {
  for (let i = 0; i < arguments.length; i++) {
    console.time(arguments[i].name);
    arguments[i](123456789);
    console.timeEnd(arguments[i].name);
  }
};

// runPerformanceTest(reverseNumber, reverseNumberWithMethods);

const isPalindrome = (num) => {
  if (num < 10) return true;

  if (num === reverseNumberWithMethods(num)) {
    return true;
  }

  return false;
};

const min = 1;
const max = 20;

for (let num = min; num < max; num++) {
  if (isPalindrome(num)) {
    console.log(num);
  }
}
