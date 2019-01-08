case class Fita(direita: List[Char], esquerda: List[Char] = Nil) {
  def dir = direita match {
    case a::b::as => Fita(b::as   , a::esquerda)
    case a::Nil   => Fita(' '::Nil, a::esquerda)
    case Nil      => Fita(' '::Nil, esquerda)
  }
  def esq = esquerda match {
    case a::as => Fita(a::direita     , as)
    case Nil   => Fita(' '::direita   , Nil)
  }
  def simbolo = direita.head
  def escreva(c: String) = Fita(c.head :: direita.tail, esquerda)
  override def toString = esquerda.reverse.mkString("") + direita.mkString("")
}

def run(state: String, fita: Fita)(implicit rules: List[List[String]]): String = {
  val a = rules.find(r => r.head == state && r(1).head == fita.simbolo)
  val b = rules.find(r => r.head == "*"   && r(1).head == fita.simbolo)
  val c = rules.find(r => r.head == state && r(1).head == '*')
  val d = rules.find(r => r.head == "*"   && r(1).head == '*')
  if (a.isDefined) a else if (b.isDefined) b else if (c.isDefined) c else d
} match {
  case Some(List(_, _, c, _, e)) if e.startsWith("halt") => (if(c == "*") fita else fita.escreva(c)).toString
  case Some(List(_, _, c, d, e)) => run(e, {
      val q = if(c == "*") fita else fita.escreva(c)
      if(d == "*") q else if(d == "r") q.dir else q.esq
    })
  case None                      => "ERR"
}

var entrada = scala.io.StdIn.readLine()
while (entrada != null) {
  val List(arq, in) = entrada.split(",").toList
  val a = io.Source.fromFile(arq).getLines
            .filter(l => !l.isEmpty && l(0)!=';')
            .map(_.split(" ")
                  .take(5)
                  .toList
                  .map(_.replace("_", " "))
                )
            .toList
  println(arq + "," + in + "," + run("0", Fita(in.toList))(a).trim)
  entrada = scala.io.StdIn.readLine()
}
