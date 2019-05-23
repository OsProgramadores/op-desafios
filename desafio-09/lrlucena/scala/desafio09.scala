val digits = ('0' to '9') ++ ('A' to 'Z') ++ ('a' to 'z')

def char2int(n: Char): BigInt = n match {
  case a if a >= 'a' => a - 'a' + 36
  case a if a >= 'A' => a - 'A' + 10
  case a             => a - '0'
}

val limit = baseNTo10("z" * 30, 62)

def baseNTo10(a: String, base: BigInt) =
  a.reverse.map(char2int).zipWithIndex.map{case (a,i) => a * base.pow(i)}.sum

def base10ToN(b: BigInt, base: BigInt, ss: List[BigInt] = Nil) : String =
  if (b == 0 && ss == Nil) "0"
  else if (b == 0)         ss.map(i => digits(i.toInt)).mkString
  else                     base10ToN(b / base, base, b % base ::ss)

def baseNToM(a: String, b1: Int, b2: Int) =
  if(b1<2 || b1>62 || b2<2 || b2>62 || a.distinct.diff(digits.take(b1))!="" || baseNTo10(a, b1)> limit) "???"
  else base10ToN(baseNTo10(a, b1), b2)

var in = io.StdIn.readLine()
while (in != null){
  val Array(b1, b2, d) = in.split(" ")
  println(baseNToM(d, b1.toInt, b2.toInt))
  in = io.StdIn.readLine()
}
