import scala.io.StdIn._

def mdc(a: Int, b: Int): Int = (a, b) match {
  case (0, b)          => b
  case (a, b) if a > b => mdc(a % b, b)
  case (a, b) if a < b => mdc(b, a)
}

def simplificar(a: Int, b: Int): String = {
  val m = mdc(a % b, b)
  if (m == b) {
    s"${a / m}"
  } else if (a > b) {
    val c = a / b
    s"${c} ${(a % b) / m}/${b / m}"
  } else {
    s"${a / m}/${b / m}"
  }
}

var entrada = readLine()
while (entrada != null) {
  entrada.split("/").map(_.toInt).toList match {
    case List(a)    => println(a)
    case List(a, 0) => println("ERR")
    case List(a, b) => println(simplificar(a, b))
  }
  entrada = readLine()
}
