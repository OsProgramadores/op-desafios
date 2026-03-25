// Crivo de Aristóteles
def crivo(a: Stream[Int]): Stream[Int] = a match {
  case p #:: xs => p #:: crivo(xs.filter(_ % p != 0))
}

// Lista de numeros primos
val primos = 2 #:: crivo(Stream.from(3, 2))

// Pegar os menores do que 100000
primos takeWhile(_ < 100000) foreach println
