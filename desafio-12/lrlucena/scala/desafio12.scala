import scala.io.StdIn._

val zero = BigInt(0)
// Todas as potencias de 2
val potencias = Stream.from(0).map(i => (zero.setBit(i), i))

var entrada = readLine()
while (entrada!=null){
  val n = BigInt(entrada)
  val a = potencias.dropWhile(_._1 < n)
  val (head, pos) = a.head
  println(s"${n} ${if(head==n) s"true ${pos}" else "false"}")
  entrada = readLine()
}
