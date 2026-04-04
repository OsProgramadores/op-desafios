import java.util.Scanner;

public class ListaPalindromos {

  public static void main(String[] args) {
    int numeroInicial;
    int numeroFinal;

    try (Scanner scanner = new Scanner(System.in)) {
      while (true) {

        System.out.print("Digite o número inicial e o final: ");

        try {
          numeroInicial = scanner.nextInt();
          numeroFinal = scanner.nextInt();

          if (numeroInicial < 0 || numeroFinal < 0) {
            System.out.println("Digite apenas números naturais");
            continue;
          }

          if (numeroInicial > numeroFinal) {
            System.out.println("O número inicial deve ser igual ou menor que o número final");
            continue;
          }

          break;

        } catch (java.util.InputMismatchException e) {
          System.out.println("Digite apenas números naturais");
          scanner.nextLine();
        }
      }
    }

    for (int i = numeroInicial; i <= numeroFinal; i++) {
      int soma = 0;
      int j = i;

      while (j > 0) {
        int ultimoAlgarismo = j % 10;
        soma = (soma * 10) + ultimoAlgarismo;
        j = j / 10;
      }

      if (soma == i) {
        System.out.println(i);
      }
    }
  }
}
