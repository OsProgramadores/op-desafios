// http://homepage.eircom.net/~reidr1/Knights-Tour.htm

val moves = List((1,2),(2,1),(2,-1),(-1,-2),(1,-2),(-2,1),(-2,-1),(-1,2))

val seq = """ABAcAte Com DEnDe FAz GranDe FArofa.
             HAja CoDiGo E CHa BEnto.
             CHA Hoje, FE aGora.
             Ha FErro E GElo.
             BiCo Bom, Hoje GAlo.
             Beba cHa e aGua, Faça GElo.
             BiFe De BACalhau.
             Bolo De Gema E Baunilha.
             Dois GarFos Grandes"""
             .filter(a => a >= 'A' && a <= 'Z')
             .map(a => moves(a - 'A')).toList

def tour(a: List[(Int, Int)], p: String = "a1"): List[String] = a match {
  case x::xs => p :: tour(xs, s"${(p(0) + x._1).toChar}${p(1) - '0' + x._2}")
  case Nil   => Nil
}

val t = tour(seq)
val p = args(0)
val a = t.dropWhile(_ != p) ++ t.takeWhile(_ != p)
println(a.mkString("\n"))
