import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Palindromos {

  int intervaloInicial;
  int intervaloFinal;
  List<Integer> palindromos;

  public Palindromos(int intervaloInicial, int intervaloFinal) {
    this.intervaloInicial = intervaloInicial;
    this.intervaloFinal = intervaloFinal;
    this.palindromos = encontrarPalindromos(intervaloInicial, intervaloFinal);
  }

  /**
   * Metodo para validar se a entrada é válida. Caso não seja, lança exceção {@code
   * IllegalArgumentException}
   *
   * @param intervaloInicial
   * @param intervaloFinal
   */
  public static void isValidInput(int intervaloInicial, int intervaloFinal) {
    if (intervaloInicial <= 0 || intervaloFinal <= 0) {
      throw new IllegalArgumentException(
          "Os valores iniciais e finais devem ser um número inteiro positivo (maior que 0).");
    }

    if (intervaloInicial > intervaloFinal) {
      throw new IllegalArgumentException(
          "O valor inicial ("
              + intervaloInicial
              + ") não pode ser maior que o valor final ("
              + intervaloFinal
              + ").");
    }
  }

  public static boolean isPalindromo(int numeroAReverter) {
    int original = numeroAReverter;
    int numeroRevertido = 0;
    while (numeroAReverter != 0) {
      int ultimoDigito = numeroAReverter % 10; // Pega o último dígito
      numeroRevertido = numeroRevertido * 10 + ultimoDigito; // Adiciona ao número reverso
      numeroAReverter /= 10; // Remove o último dígito
    }
    return original == numeroRevertido;
  }

  public static List<Integer> encontrarPalindromos(int intervaloInicial, int intervaloFinal) {

    ArrayList palindromos = new ArrayList<>();
    for (int i = intervaloInicial; i <= intervaloFinal; i++) {
      if (i < 10) {
        palindromos.add(i);
      } else if (isPalindromo(i)) {
        palindromos.add(i);
      }
    }

    return palindromos;
  }

  @Override
  public java.lang.String toString() {
    String resultadoFormatado =
        String.join(", ", palindromos.stream().map(Object::toString).toList());
    return resultadoFormatado;
  }

  public static void main(String[] args) {
    int intervaloInicial = 0;
    int intervaloFinal = 0;

    Scanner scanner = new Scanner(System.in);

    boolean entradaValida = false;

    if (args.length >= 1) {
      try {
        intervaloInicial = Integer.parseInt(args[0]);
        intervaloFinal = Integer.parseInt(args[1]);
        entradaValida = true;
      } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
        System.err.println("Argumentos devem ser números inteiros válidos.");
      }
    }

    while (!entradaValida) {
      System.out.println("Entrada inválida. Informe inteiros válidos: ");
      try {
        if (intervaloInicial == 0) {
          System.out.print("Primeiro número: ");
          intervaloInicial = scanner.nextInt();
        }
        System.out.print("Segundo número: ");
        intervaloFinal = scanner.nextInt();

        isValidInput(
            intervaloInicial,
            intervaloFinal); // Verifica se a entrada é válida, inteiro positivo, sendo que inicial
                             // menor que final

        entradaValida = true; // Sai do loop se a leitura for bem-sucedida

      } catch (InputMismatchException e) {
        System.out.println("Entrada inválida. Por favor, digite apenas números inteiros.");
        scanner.next(); // Limpa o buffer do Scanner para evitar loop infinito
      }
    }
    scanner.close(); // Fecha o scanner após receber uma entrada válida

    Palindromos palindromos = new Palindromos(intervaloInicial, intervaloFinal);
    System.out.println(palindromos);
  }
}
