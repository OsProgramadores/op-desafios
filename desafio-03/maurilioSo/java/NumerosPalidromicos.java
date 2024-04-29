import java.util.InputMismatchException;
import java.util.Scanner;

public class NumerosPalindromicos {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    try {
      System.out.print("Digite o primeiro número: ");
      long numeroInicial = sc.nextLong();
      System.out.print("Digite o último número: ");
      long numeroFinal = sc.nextLong();

      if (numeroInicial < 0 || numeroFinal < 0) {
        System.out.println("Você deve informar 2 números inteiros positivos!");
      } else if (numeroInicial > numeroFinal) {
        System.out.println("O primeiro número deve ser menor que o segundo número!");
      } else {
        System.out.println("Os palindrômicos do intervalo entre " + numeroInicial + " e " + numeroFinal + " : ");
        for (long i = numeroInicial; i <= numeroFinal; i++) {
          if (verificarPalindromico(i)) {
            System.out.println(i);
          }
        }
      }
    } catch (InputMismatchException e) {
      System.out.println("Os números devem ser inteiros, com no máximo 64 bits!");
    }
    sc.close();
  }

  public static boolean verificarPalindromico(long numero) {
    long original = numero;
    long numeroInvertido = 0;
    while (numero != 0) {
      long resto = numero % 10;
      numeroInvertido = numeroInvertido * 10 + resto;
      numero /= 10;
    }
    return original == numeroInvertido;
  }
}
