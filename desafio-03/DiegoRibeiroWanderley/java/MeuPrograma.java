public class MeuPrograma {
  public static void main(String[] args) {

    int numeroComeco = Integer.parseInt(args[0]);
    int numeroFim = Integer.parseInt(args[1]);

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
