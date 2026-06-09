public class MeuPrograma {
  public static void main(String[] args) {

    if (args.length != 2) {
      System.out.println("ERRO: O programa deve receber exatamente 2 parâmetros");
      System.exit(1);
    }

    int numeroComeco = Integer.parseInt(args[0]);
    int numeroFim = Integer.parseInt(args[1]);

    if (numeroComeco < 0 || numeroFim < 0) {
      System.out.println("ERRO: Ambos os limites devem ser positivos");
      System.exit(1);
    }

    for (int i = numeroComeco; i <= numeroFim; i++) {

      int numeroInvertido = 0;
      int numeroTemporario = i;

      while (numeroTemporario > 0) {
        int ultimoDigito = numeroTemporario % 10;
        numeroInvertido = (numeroInvertido * 10) + ultimoDigito;
        numeroTemporario /= 10;
      }

      if (i == numeroInvertido) {
        System.out.println(i);
      }
    }
  }
}
