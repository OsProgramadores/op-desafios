import sequtils

proc isPalindrome(num: uint64): bool = 
  var n = num
  var digits : seq[uint64]
  while n > 0'u64:
    digits.add(n mod 10)
    n = n div 10
  if digits.len == 0: digits.add(0)

  for i, item in digits:
    if item != digits[digits.high-i]:
      return false
  return true

proc checkRange(a, b:uint64) : seq[uint64] =
  let nums = (a..b).toSeq()
  nums.filter(isPalindrome)

echo checkRange(3000,3010)
