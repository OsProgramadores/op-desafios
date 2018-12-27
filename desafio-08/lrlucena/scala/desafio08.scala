def mdc(a: Int, b: Int): Int = (a, b) match {
  case (0, b) => b
  case (a, b) => mdc(b % a, a)
}

def simplificar(a: Int, b: Int): String = {
  val (c, d) = (a / b, a % b)
  val m = mdc(d, b)
  (if (c == 0) "" else s"${c} ") + (if (d == 0) "" else s"${d / m}/${b / m}")
}

var entrada = scala.io.StdIn.readLine()
while (entrada != null) {
  println {
    entrada.split("/").map(_.toInt).toList match {
      case List(a)    => a
      case List(a, 0) => "ERR"
      case List(a, b) => simplificar(a, b)
    }
  }
  entrada = scala.io.StdIn.readLine()
}
