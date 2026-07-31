import java.util.Scanner;

public class MeuDesafio03 {

  public static boolean ehPalindromo(long numero) {
    String texto = Long.toUnsignedString(numero);
    String reverso = new StringBuilder(texto).reverse().toString();
    return texto.equals(reverso);
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Digite o valor inicial: ");
    long inicio = lerNumero(scanner);

    System.out.print("Digite o valor final: ");
    long fim = lerNumero(scanner);

    if (Long.compareUnsigned(inicio, fim) > 0) {
      System.out.println("O valor inicial deve ser menor ou igual ao valor final.");
      scanner.close();
      return;
    }

    System.out.println(
        "Números palíndromos entre "
            + Long.toUnsignedString(inicio)
            + " e "
            + Long.toUnsignedString(fim)
            + ":");

    for (long i = inicio; Long.compareUnsigned(i, fim) <= 0; i++) {
      if (ehPalindromo(i)) {
        System.out.println(Long.toUnsignedString(i));
      }
      // Interrompe em 2^64 - 1 para evitar overflow no incremento.
      if (i == -1L) {
        break;
      }
    }

    scanner.close();
  }

  private static long lerNumero(Scanner scanner) {
    while (true) {
      try {
        return Long.parseUnsignedLong(scanner.nextLine().trim());
      } catch (NumberFormatException e) {
        System.out.print("Valor inválido. Digite um número inteiro positivo: ");
      }
    }
  }
}
