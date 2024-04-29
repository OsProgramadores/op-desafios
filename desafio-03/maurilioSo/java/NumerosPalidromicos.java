import java.util.InputMismatchException;
import java.util.Scanner;

public class NumerosPalidromicos {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    try {
      System.out.print("Digite o primeiro numero: ");
      long numeroInicial = sc.nextLong();
      System.out.print("Digite o ultimo numero: ");
      long numeroFinal = sc.nextLong();

      if (numeroInicial < 0 || numeroFinal < 0) {
        System.out.println("Você deve informar 2 números inteiros positivos!");
      } else if (numeroInicial > numeroFinal) {
        System.out.println("O primeiro número deve ser menor que o segundo número!");
      } else {
        System.out.println("Os polindrômicos do intervalo entre " + numeroInicial + " e " + numeroFinal + " : ");
        for (long i = numeroInicial; i <= numeroFinal; i++) {
          if (i == verificarPalidromico(i)) {
            System.out.println(i);
          }

        }

      }
    } catch (InputMismatchException e) {
      System.out.println("Os números devem ser inteiros, com no maximo 64 bits!");
    }

    sc.close();
  }

  public static long verificarPalidromico(long numero) {
    long numeroInvertido = 0;
    long resto;
    while (numero != 0) {
      resto = numero % 10;
      numeroInvertido = numeroInvertido * 10 + resto;
      numero /= 10;
    }

    return numeroInvertido;
  }

}
