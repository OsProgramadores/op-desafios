def clean(s: String) = s.toUpperCase.filter(c => c >= 'A' && c <= 'Z')

implicit class D(r: String) { def -(s: String) = r.toSeq.diff(s).unwrap }

def anagrams(input: String, words: List[String], list: List[String] = Nil): List[String] =
  if (input.nonEmpty)
    words.tails.flatMap {
      case wrds @ word :: _ =>
        val unusedLetters = input - word
        anagrams(unusedLetters, wrds.filter(_ - unusedLetters == ""), word :: list)
      case _ => Nil
    }.toList
  else List(list.reverse.mkString(" "))

val input = clean(args.headOption.getOrElse("oi gente"))
val words = io.Source.fromFile("words.txt").getLines().filter(_ - input == "").toList.sorted

println(anagrams(input, words).mkString("\n"))
