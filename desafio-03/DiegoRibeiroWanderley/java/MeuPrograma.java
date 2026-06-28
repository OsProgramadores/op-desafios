public class MeuPrograma {
  public static void main(String[] args) {

    if (args.length != 2) {
      System.out.println("ERRO: O programa deve receber exatamente 2 parâmetros");
      System.exit(1);
    }

    long numeroComeco = 0L;
    long numeroFim = 0L;

    try {
      numeroComeco = Long.parseLong(args[0]);
      numeroFim = Long.parseLong(args[1]);
    } catch (NumberFormatException e) {
      System.out.println("ERRO: Ambos os argumentos devem ser números");
      System.exit(1);
    }

    if (numeroComeco < 0 || numeroFim < 0) {
      System.out.println("ERRO: Ambos os limites devem ser positivos");
      System.exit(1);
    }

    if (numeroComeco > numeroFim) {
      System.out.println("ERRO: O intervalo estabelecido está incorreto");
      System.exit(1);
    }

    for (long i = numeroComeco; i <= numeroFim; i++) {

      long numeroInvertido = 0L;
      long numeroTemporario = i;

      while (numeroTemporario > 0) {
        long ultimoDigito = numeroTemporario % 10;
        numeroInvertido = (numeroInvertido * 10) + ultimoDigito;
        numeroTemporario /= 10;
      }

      if (i == numeroInvertido) {
        System.out.println(i);
      }
    }
  }
}
