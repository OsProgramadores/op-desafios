import strutils, sequtils, strformat, bigints

let file = readFile("d12.txt")
let nums = file.splitWhiteSpace.mapIt(it.initBigInt)

proc getExpoent(n:BigInt) : string =
  var num = 1.initBigInt
  var exp : int = 0
  while num < n:
    num*=2
    inc exp
  if n==num:
    return fmt"{n} true {exp}"
  elif n==1:
    return fmt"{n} true 0"
  else:
    return fmt"{n} false"

for n in nums:
  echo getExpoent(n)
