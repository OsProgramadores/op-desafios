import java.util.Scanner;

public class Palindromo {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Escolha o número inicial: ");
    int n1 = sc.nextInt();
    System.out.println("Escolha o numero final: ");
    int n2 = sc.nextInt();
    for (int i = n1; i <= n2; i++) {
      if (ehPalindromo(i)) {
        System.out.print(i + " ");
      }
    }
  }

  public static boolean ehPalindromo(int numero) {
    String numeroStr = String.valueOf(numero);
    StringBuilder sb = new StringBuilder(numeroStr).reverse();
    return numeroStr.equals(sb.toString());
  }
}
