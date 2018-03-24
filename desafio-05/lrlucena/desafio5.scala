import scala.util.parsing.json.JSON
import scala.io.Codec.UTF8

object Desafio5 extends App {
  case class Funcionario(input: Map[String, String]) {
    def id = input("id")
    def nome = input("nome")
    val sobrenome = input("sobrenome")
    val salario = input("salario").asInstanceOf[Double]
    val area = areas(input("area"))
    val nomeCompleto = s"${nome} ${sobrenome}"
    def salariof = format(salario)
  }

  type MJson = Map[String, List[Map[String, String]]]
  val entrada = io.Source.fromFile(args(0))(UTF8).mkString
  val json = JSON.parseFull(entrada).get.asInstanceOf[MJson]
  val areas = json("areas").map { case a => a("codigo") -> a("nome") }.toMap
  val funcionarios = json("funcionarios").map(Funcionario)

  def min[T](f: T => Double)(list: List[T]) = list.takeWhile(f(_) == f(list.head))
  def max[T](f: T => Double)(list: List[T]) = list.dropWhile(f(_) < f(list.last))
  def avg(list: List[Funcionario]) = format(list.map(_.salario).sum / list.length)

  val minSalario = min[Funcionario](_.salario) _
  val maxSalario = max[Funcionario](_.salario) _

  def format(d: Double) = "%.2f".formatLocal(java.util.Locale.US, d)

  def imprimir(text: String, list: List[Funcionario]) = for (a <- list) {
    println(s"${text}|${a.nomeCompleto}|${a.salariof}")
  }

  // Questao 1
  val global = funcionarios.sortBy(_.salario)
  imprimir("global_max", maxSalario(global))
  imprimir("global_min", minSalario(global))
  println(s"global_avg|${avg(global)}")

  // Questao 2
  val porArea = global.groupBy(_.area)
  for ((area, fun) <- porArea) {
    imprimir(s"area_max|${area}", maxSalario(fun))
    imprimir(s"area_min|${area}", minSalario(fun))
    println(s"area_avg|${area}|${avg(fun)}")
  }

  //Questao 3
  val employees = porArea.mapValues(_.length).toList.sortBy(_._2)
  val most = max[(String, Int)](_._2)(employees)
  val least = min[(String, Int)](_._2)(employees)
  for (a <- most) println(s"most_employees|${a._1}|${a._2}")
  for (a <- least) println(s"least_employees|${a._1}|${a._2}")

  // Questao 4
  val porSobreNome = global.groupBy(_.sobrenome).filter(_._2.length > 1)
  for ((sobrenome, fun) <- porSobreNome; f <- maxSalario(fun)) {
    println(s"last_name_max|${sobrenome}|${f.nomeCompleto}|${f.salariof}")
  }
}
