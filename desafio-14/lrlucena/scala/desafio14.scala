import scala.io.StdIn.readLine
import scala.util.{Try, Success, Failure}

def eval(s: String) = eval2(tokens(s))

// Removing parentheses
def eval2(tokens: List[String]): Try[String] = Try {
  val i = tokens.indexWhere(_ == ")")
  val j = tokens.take(i).lastIndexWhere(_ == "(")
  if (i >= 0) {
    val ev = eval2(tokens.drop(j + 1).take(i - j - 1)).get
    eval2(tokens.patch(j, List(ev), i - j + 1)).get
  } else
    eval1(tokens).get
}

def eval1(tokens: List[String]): Try[String] = Try {
  val m = nextOp(tokens)
  if (m >= 0) {
    val (a, b) = (tokens(m - 1).toInt, tokens(m + 1).toInt)
    val op = operation(tokens(m))(a, b).toString
    eval1(tokens.patch(m - 1, List(op), 3)).get
  } else if (tokens.length == 1)
    tokens.head
  else ???
}

// Position of the next operation to evaluate
def nextOp(tokens: List[String]): Int = {
  val i = tokens.lastIndexWhere(_ == "^")
  val j = tokens.indexWhere("*/".contains)
  val k = tokens.indexWhere("+-".contains)
  if (i >= 0) i else if (j >= 0) j else k
}

def operation(s: String)(x: Int, y: Int): Int = s match {
  case "+" => x + y
  case "-" => x - y
  case "/" => x / y
  case "*" => x * y
  case "^" => Math.pow(x, y).toInt
  case  _  => ???
}

def tokens(s: String): List[String] = s.toList match {
  case Nil                 => Nil
  case ' ' :: _            => tokens(s.tail)
  case a::as if !a.isDigit => a.toString :: tokens(s.tail)
  case _ => s.takeWhile(_.isDigit) :: tokens(s.dropWhile(_.isDigit))
}

var input = readLine()
while (input != null) {
  val value = eval(input) match {
    case Success(n)                      => n
    case Failure(_ :ArithmeticException) => "ERR DIVBYZERO"
    case Failure(_)                      => "ERR SYNTAX"
  }
  println(value)
  input = readLine()
}
