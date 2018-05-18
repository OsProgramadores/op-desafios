object Xadrez extends App {
  val peças = List("", "Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei")

  def readLines(n: Int) = (1 to n).map(_ => io.StdIn.readLine())

  // Ler 8 linhas e juntar em um texto, depois transformar em números
  val tabuleiro = readLines(8).mkString.map(_ - '0')

  // Varrer o tabuleiro e selecionar as peças de cada tipo, depois contar
  for(i <- 1 to 6) {
    val num = tabuleiro.filter(_ == i).length
    println(s"${peças(i)}: ${num} peças")
  }
}
