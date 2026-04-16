public class ListaPalindromos {

  public static void main(String[] args) {

    int numeroInicial;
    int numeroFinal;

    if (args.length != 2) {
      System.out.println("Formato de uso: java ListaPalindromos <numeroInicial> <numeroFinal>");
      return;
    }

    try {
      numeroInicial = Integer.parseInt(args[0]);
      numeroFinal = Integer.parseInt(args[1]);

      if (numeroInicial < 0 || numeroFinal < 0) {
        System.out.println("Digite apenas números naturais");
        return;
      }

      if (numeroInicial > numeroFinal) {
        System.out.println("O número inicial deve ser igual ou menor que o número final");
        return;
      }

    } catch (NumberFormatException e) {
      System.out.println("Digite apenas números naturais");
      return;
    }

    for (int i = numeroInicial; i <= numeroFinal; i++) {
      int numeroInvertido = 0;
      int j = i;

      while (j > 0) {
        int ultimoAlgarismo = j % 10;
        numeroInvertido = (numeroInvertido * 10) + ultimoAlgarismo;
        j = j / 10;
      }

      if (numeroInvertido == i) {
        System.out.println(i);
      }
    }
  }
}
