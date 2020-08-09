def clean(s: String) = s.toUpperCase.filter(c => c >= 'A' && c <= 'Z')

def contains(letters: String)(word: String) = (word - letters).isEmpty

def readFile(name: String) = io.Source.fromFile("words.txt").getLines()

implicit class D(r: String) {
  def -(s: String) = r.toSeq.diff(s).unwrap
}

def anagrams(input: String, words: List[String], list: List[String] = Nil): Unit = input match {
  case "" => println(list.sorted.mkString(" "))
  case _  => for (word :: wrds <- words.tails) {
               val unusedInput = input - word
               anagrams(unusedInput, wrds.filter(contains(unusedInput)), word :: list) }}

val input = clean(args.headOption.getOrElse("oi gente"))
val words = readFile("words.txt").filter(contains(input)).toList.sortBy(_.length).reverse

anagrams(input, words)
