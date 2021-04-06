def mdc(a: Int, b: Int): Int = if (a == 0) b else mdc(b % a, a)

def simplificar(a: Int, b: Int = 1): String = {
  val (c, d) = (a / b, a % b)
  val m = mdc(d, b)
  (if (c == 0) "" else s"${c} ") + (if (d == 0) "" else s"${d / m}/${b / m}")
}

var entrada = scala.io.StdIn.readLine()
while (entrada != null) {
  entrada.split("/").map(_.toInt).toList match {
    case List(a)    => println(a)
    case List(a, 0) => println("ERR")
    case List(a, b) => println(simplificar(a, b))
  }
  entrada = scala.io.StdIn.readLine()
}
