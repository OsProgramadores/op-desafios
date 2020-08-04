implicit class D(r: String) { def -(s: String) = r.toSeq.diff(s).unwrap }
def clean(s: String) = s.toUpperCase.filter(c => c >= 'A' && c <= 'Z')
def contains(letters: String)(word: String) = (word - letters).isEmpty

def anagrams(input: String, words: List[String], list: List[String] = Nil): Iterator[String] =
  if (input.isEmpty)
    Iterator(list.reverse.mkString(" "))
  else 
    words.tails.flatMap {
      case word :: wrds =>
        val unusedInput = input - word
        anagrams(unusedInput, wrds.filter(contains(unusedInput)), word :: list)
      case _ => Nil
    }

val input = clean(args.headOption.getOrElse("oi gente"))
val words = io.Source.fromFile("words.txt").getLines().filter(contains(input)).toList.sorted

println(anagrams(input, words).mkString("\n"))
