import scala.collection.mutable.HashMap
import scala.io.Source

case class Funcionario(id: String, nome: String, sobrenome: String, salario: Double, area: String) {
  def nomeCompleto = s"${nome} ${sobrenome}"
  def sal = salario formatted "%.2f"
}

object Desafio05 extends App {
  def parse[A](stream: Iterator[String], field: String) = {
    var str = ""
    def inc(s: String) = {
      str = str + s
      val index = str.indexOf('}')
      val (line, new_str) = str.splitAt(index + 1)
      str = new_str
      if(line.isEmpty || line.contains(']'))
        None
      else
        Some(line.dropRight(1).dropWhile(_ != '"').replace(':',',').split(",").map(_.stripSuffix("\"").stripPrefix("\"")))
    }
    stream.dropWhile(!_.contains(s""""${field}":[""")).drop(1)
      .takeWhile(!_.contains("""["""))
      .flatMap(inc _)
  }

  def calc(f: Funcionario, grupo: String, h: scala.collection.mutable.Map[String, List[Funcionario]], comp: (Double, Double) => Boolean) ={
    h(grupo) match {
      case Nil                              => h(grupo) = List(f)
      case l if comp(l.head.salario, f.salario) =>
      case l if f.salario == l.head.salario => h(grupo) = f::l
      case l                                => h(grupo) = List(f)
    }
  }

  val stream = Source.fromFile(args(0)).getLines()
  val stream2 = Source.fromFile(args(0)).getLines()

  val menores, maiores, sobrenome = HashMap[String, List[Funcionario]]().withDefault(l => List[Funcionario]())
  val soma = HashMap[String, Double]().withDefault(l => 0.0)
  val quantidade, qSobrenome = HashMap[String, Int]().withDefault(l => 0)

  val areas = parse(stream2, "areas").map(f => (f(1), f(3))).toMap.withDefault(l => "***Error***")
  val funcionarios = parse(stream, "funcionarios").map(f => Funcionario(f(1), f(3), f(5), f(7).toDouble, f(9)))

  funcionarios.foreach{ f =>
    // Questao 1
    calc(f, "", menores, _ < _)
    calc(f, "", maiores, _ > _)
    soma("") = soma("") + f.salario
    quantidade("") = quantidade("") + 1

    // Questao 2
    calc(f, f.area, menores, _ < _)
    calc(f, f.area, maiores, _ > _)
    soma(f.area) = soma(f.area) + f.salario

    // Questao 3
    quantidade(f.area) = quantidade(f.area) + 1

    // Questao 4
    calc(f, f.sobrenome, sobrenome, _ > _)
    qSobrenome(f.sobrenome) = qSobrenome(f.sobrenome) + 1
  }

  // Questao 1
  for (f <- menores("")){
    println(s"global_min|${f.nomeCompleto}|${f.sal}")
  }

  for (f <- maiores("")){
    println(s"global_max|${f.nomeCompleto}|${f.sal}")
  }

  println(s"global_avg|${soma("") / quantidade("") formatted "%.2f"}")

  // Questao 2
  for(area <- areas) {
    for(f <- maiores(area._1)) {
      println(s"area_max|${area._2}|${f.nomeCompleto}|${f.sal}")
    }
    for(f <- menores(area._1)) {
      println(s"area_min|${area._2}|${f.nomeCompleto}|${f.sal}")
    }
  }

  for((cod, valor) <- soma if cod != "") {
    println(s"area_avg|${areas(cod)}|${valor / quantidade(cod) formatted "%.2f"}")
  }

  // Questao 3
  for((cod, quant) <- quantidade.toList.groupBy(_._2).head._2){
    println(s"least_employees|${areas(cod)}|${quant}")
  }

  for((cod, quant) <- quantidade.toList.groupBy(_._2).takeRight(2).head._2){
    if (cod.nonEmpty)
      println(s"most_employees|${areas(cod)}|${quant}")
  }

  // Questao 4
  for((sobre, funs) <- sobrenome; fun <- funs if qSobrenome(sobre) > 1) {
    println(s"last_name_max|${sobre}|${fun.nomeCompleto}|${fun.sal}")
  }
}
