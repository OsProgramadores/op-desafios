import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;

public class Palindromos {

  int intervaloInicial;
  int intervaloFinal;
  List<Integer> palindromos;

  public Palindromos(int intervaloInicial, int intervaloFinal) {
    this.intervaloInicial = intervaloInicial;
    this.intervaloFinal = intervaloFinal;
    this.palindromos = new ArrayList<>();
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
          "Os valores iniciais e finais devem ser números inteiros positivos (maior que 0).");
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

  public void encontrarPalindromos(int intervaloInicial, int intervaloFinal) {
    for (int i = intervaloInicial; i <= intervaloFinal; i++) {
      if (i < 10) {
        this.palindromos.add(i);
      } else if (isPalindromo(i)) {
        this.palindromos.add(i);
      }
    }
  }

  public void imprimirPalindromos() {
    try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out))) {
      for (int palindromo : palindromos) {
        writer.write(String.valueOf(palindromo));
        writer.newLine();
      }
    } catch (IOException e) {
      throw new RuntimeException("Erro ao tentar escrever os palíndromos no console.", e);
    }
  }
  ;

  public static void main(String[] args) {
    int intervaloInicial = 0;
    int intervaloFinal = 0;

    // Valida se é uma entrada válida
    try {
      // Deve possuir 2 argumentos
      if (args == null || args.length != 2) {
        throw new InputMismatchException();
      }
      // Devem ser inteiros válidos
      intervaloInicial = Integer.parseInt(args[0]);
      intervaloFinal = Integer.parseInt(args[1]);
      // Intervalo final deve ser maior que o inicial
      isValidInput(intervaloInicial, intervaloFinal);
    } catch (NumberFormatException | InputMismatchException e) {
      System.err.println(
          "Ao executar o programa, você deve informar dois números inteiros válidos");
      System.exit(1);
    }

    // Se a entrada for válida, instancia o objeto palindromos com uma lista vazia de palindromos
    Palindromos palindromos = new Palindromos(intervaloInicial, intervaloFinal);
    palindromos.encontrarPalindromos(intervaloInicial, intervaloFinal);
    palindromos.imprimirPalindromos();
  }
}
