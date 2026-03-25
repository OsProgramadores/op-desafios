import scala.io.StdIn._
val a = readLine
val b = readLine
val a_r = a.toDouble
val b_r = b.toDouble

def f(s: String) = s.take((s.length + 1) / 2).toInt / s.take(1).toInt
val x = f(a)
val y = f(b) * 10

for(i<- x to y) {
  val s = s"${i}${i.toString.reverse.drop(1)}"
  if (a_r <= s.toDouble && s.toDouble <= b_r) println(s)
  val r = s"${i}${i.toString.reverse}"
  if (a_r <= r.toDouble && r.toDouble <= b_r) println(r)
}
