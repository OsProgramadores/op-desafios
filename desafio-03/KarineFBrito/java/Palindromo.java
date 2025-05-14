import java.util.Scanner;

public class Palindromo {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Escolha o número inicial: ");
    int n1 = sc.nextInt();
    System.out.println("Escolha o numero final: ");
    int n2 = sc.nextInt();
    if (n1 < 0 || n2 < 0) {
      System.out.println("Os números não podem ser negativos!");
      sc.close();
      System.exit(0);
    }
    if (n1 >= n2) {
      System.out.println("O número inicial não pode ser maior ou igual que o final!");
      sc.close();
      System.exit(0);
    }
    for (int i = n1; i <= n2; i++) {
      if (ehPalindromo(i)) {
        System.out.print(i + " ");
      }
    }
  }

  public static boolean ehPalindromo(int numero) {
    if (numero >= 0 && numero < 10) {
      return true;
    }
    String numeroStr = String.valueOf(numero);
    StringBuilder sb = new StringBuilder(numeroStr).reverse();
    return numeroStr.equals(sb.toString());
  }
}
