object Desafio6 extends App {

  def clean(s: String) = s.toUpperCase.filter(c => c >= 'A' && c <= 'Z')

  def anagrams(input: String, words: List[String], list: List[String] = Nil): List[String] = {
    var wrds = words
    if (input.nonEmpty)
      words.flatMap { word =>
        wrds = wrds.tail
        val w = input diff word
        anagrams(w, wrds.filter(_.diff(w)==""), word :: list)
      }
    else List(list.reverse.mkString(" "))
  }

  val input = clean(args.headOption.getOrElse("oi gente"))

  val words = io.Source.fromFile("words.txt").getLines.toList.filter(_.diff(input) == "").sorted
  //.fromURL("https://osprogramadores.com/desafios/d06/words.txt")

  val a = anagrams(input, words).mkString("\n")
  println(a)
}
