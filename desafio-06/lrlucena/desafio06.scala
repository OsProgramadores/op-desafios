object Desafio6 extends App {

  implicit class Texto(s: String) {
    def clean: String = s.toUpperCase.filter(c => c >= 'A' && c <= 'Z')

    def bag: Map[Char, Int] =
      s.groupBy(c => c).map { case (a, b) => (a, b.length) } withDefaultValue 0

    def subtr(b: String): Map[Char, Int] = {
      val (sb, bb) = (s.bag, b.bag)
      sb ++ (bb map { case (c, i) => c -> (sb(c) - i) })
    }

    def holds(b: String): Boolean = s.subtr(b).values.forall(_ >= 0)

    def -(b: String): String = if (s holds b)
      s.subtr(b).map { case (c, i) => c.toString * i }.mkString
    else ""
  }

  def anagrams(input: String, words: List[String], list: List[String] = Nil): List[String] = {
    var wrds = words
    if (input.nonEmpty)
      words.flatMap { word =>
        wrds = wrds.dropWhile(_ <= word)
        val w = input - word
        anagrams(w, wrds.filter(w.holds), word :: list)
      }
    else List(list.reverse.mkString(" "))
  }

  val input = args.headOption.getOrElse("oi gente").clean

  val words = io.Source.fromFile("words.txt").getLines.toList.filter(input.holds).sorted
  //.fromURL("https://osprogramadores.com/desafios/d06/words.txt")

  val a = anagrams(input, words).mkString("\n")
  println(a)
}
