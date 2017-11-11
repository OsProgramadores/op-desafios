object Desafio06 extends App {
  type MapCI = Map[Char, Int]

  def letras(s: String) =
    (s.groupBy(c => c) map { case (a, b) => (a, b.length) }) withDefaultValue 0

  def subtrair(a: MapCI, b: MapCI) = a ++ 
    (b map {
      case (c, i) => c -> (a(c) - i)}) filter {
      case (_, i) => i != 0} withDefaultValue 0

  def contem(a: MapCI, b: MapCI) = subtrair(a, b).values.forall(_ > 0)

  val palavras = io.Source
    .fromURL("https://osprogramadores.com/desafios/d06/words.txt")
    //.fromFile("words.txt")
    .getLines
    .toList
    .map { case p => (p, letras(p)) }

  def anagramas(lista: List[String], s: MapCI, palavras: List[(String, MapCI)]): List[List[String]] = {
    if (s == Map()) List(lista)
    else {
      palavras filter {
        case p => contem(s, p._2)
      } map {
        case p =>
          anagramas(p._1 :: lista, subtrair(s, p._2), palavras.dropWhile(a => a._1 < p._1))
      } flatten()
    }
  }

  val entrada = letras("VERMELHO".toUpperCase().filter(c => c >= 'A' && c <= 'Z'))
  val ana = anagramas(Nil, entrada, palavras.filter(p => contem(entrada, p._2)))
    .map(_.reverse.mkString(" "))
    .mkString("\n")
  println(ana)
}
