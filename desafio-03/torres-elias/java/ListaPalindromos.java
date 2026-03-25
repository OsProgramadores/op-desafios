import java.util.Scanner;

public class ListaPalindromos {

  public static void main(String[] args) {
    int numeroInicial;
    int numeroFinal;

    try (Scanner scanner = new Scanner(System.in)) {
      System.out.print("Digite o número inicial e o final: ");
      numeroInicial = scanner.nextInt();
      numeroFinal = scanner.nextInt();
    }

    for (int i = numeroInicial; i <= numeroFinal; i++) {
      String numeroOriginal = String.valueOf(i);
      String numeroInvertido = new StringBuilder(numeroOriginal).reverse().toString();

      if (numeroOriginal.equals(numeroInvertido)) {
        System.out.println(i);
      }
    }
  }
}
