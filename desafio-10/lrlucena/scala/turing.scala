// Fita infinita
case class Fita(direita: List[Char], esquerda: List[Char] = Nil) {
  def moverDireita = direita match {
    case a::b::as => Fita(b::as   , a::esquerda)
    case a::Nil   => Fita(' '::Nil, a::esquerda)
    case Nil      => Fita(' '::Nil, esquerda)
  }
  def moverEsquerda = esquerda match {
    case a::as => Fita(a::direita     , as)
    case Nil   => Fita(' '::direita   , Nil)
  }
  def simbolo = direita.head.toString
  def escreva(c: String) = Fita(c.head :: direita.tail, esquerda)
  override def toString = (esquerda.reverse ++ direita).mkString.trim
}

// Constantes
val HALT = "halt"; val ERRO = "ERR"; val VIRGULA = ","; val ESPACO = " "; val SUB = "_"
val * = "*"; val COMENTARIO = ';'; val Regra0 = "0"; val DIR = "r"; val ESQ = "l"
val DOIS = 2; val CINCO = 5

// Devolve a regra que será aplicada de acordo com o estado atual a posição da fita
def regra(estado: String, simbolo: String)(implicit regras: List[List[String]]) =
  List(List(estado, simbolo), List(*, simbolo), List(estado, *), List(*, *))
    .map(r => regras.find(_.take(DOIS) == r))   // Achar as regras
    .reduce(_ orElse _)                         // Escolher de acordo com prioridade
    .map(_.drop(DOIS))                          // Devolver a ação a realizar

// Executa a próxima regra de acordo com o estado atual a posição da fita
def run(fita: Fita, estado: String = Regra0)(implicit regras: List[List[String]]): String = regra(estado, fita.simbolo) match {
  case Some(List(c  , _, e)) if e.startsWith(HALT) => fita.escreva(c).toString
  case Some(List(*, _, e))   if e.startsWith(HALT) => fita.toString
  case Some(List(c, d, e))                         => run ({
      val f = if (c == *) fita else fita.escreva(c)
      d match {case DIR => f.moverDireita case ESQ => f.moverEsquerda case _ => f}
    }, e)
  case _                                           => ERRO
}

// Lê um arquivo de regras
def lerRegras(arq: String) = io.Source.fromFile(arq).getLines.toList
      .map(linha => linha.takeWhile(_ != COMENTARIO))  // Elimina os comentários
      .filter(l => !l.trim.isEmpty)                    // Remove as linhas em branco
      .map(_.split(ESPACO).take(CINCO).map(_.replace(SUB, ESPACO)).toList)

// Programa principal
var entrada = io.StdIn.readLine()
while (entrada != null) {
  val Array(arq, in) = entrada.split(VIRGULA)
  val out = run(Fita(in.toList))(lerRegras(arq))
  println(List(arq, in, out).mkString(VIRGULA))
  entrada = io.StdIn.readLine()
}
