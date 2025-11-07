import java.util.ArrayList;
import java.util.List;

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
  public void isValidInput(int intervaloInicial, int intervaloFinal) {
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

  private boolean isPalindromo(int numeroAReverter) {
    int original = numeroAReverter;
    int numeroRevertido = 0;
    while (numeroAReverter != 0) {
      int ultimoDigito = numeroAReverter % 10; // Pega o último dígito
      numeroRevertido = numeroRevertido * 10 + ultimoDigito; // Adiciona ao número reverso
      numeroAReverter /= 10; // Remove o último dígito
    }
    return original == numeroRevertido;
  }

  List<Integer> encontrarPalindromos(int intervaloInicial, int intervaloFinal) {
    isValidInput(intervaloInicial, intervaloFinal);
    palindromos = new ArrayList<>();
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

    if (args != null && args.length >= 1) {
      try {
        intervaloInicial = Integer.parseInt(args[0]);
        intervaloFinal = Integer.parseInt(args[1]);
      } catch (NumberFormatException e) {
        System.err.println("Argumentos devem ser números inteiros válidos.");
        System.err.println("Detalhe: " + e.getMessage());
      }
    }

    Palindromos palindromos = new Palindromos(intervaloInicial, intervaloFinal);
    System.out.println(palindromos);
  }
}
