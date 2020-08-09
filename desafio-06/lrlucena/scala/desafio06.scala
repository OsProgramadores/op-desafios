import io.Source.fromFile

implicit class D(r: String) { def -(s: String) = r.toSeq.diff(s).unwrap }
def clean(s: String) = s.toUpperCase.filter(c => c >= 'A' && c <= 'Z')
def contains(letters: String)(word: String) = (word - letters).isEmpty

def anagrams(input: String, words: List[String], list: List[String] = Nil): Unit = input match {
  case "" => println(list.mkString(" "))
  case _  => for (word :: wrds <- words.tails) {
               val unusedInput = input - word
               anagrams(unusedInput, wrds.filter(contains(unusedInput)), word :: list) }}

val input = clean(args.headOption.getOrElse("oi gente"))
val words = fromFile("words.txt").getLines().filter(contains(input)).toList.sorted.reverse

anagrams(input, words)
