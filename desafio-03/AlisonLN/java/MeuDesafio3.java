import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MeuDesafio3 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    List<String> numPalindromo = new ArrayList<>();

    int numeroInicial;
    int numeroFinal;
    while (true) {
      System.out.println("Digite Numero Inicial");
      numeroInicial = sc.nextInt();
      System.out.println("Digite Numero Final");
      numeroFinal = sc.nextInt();

      if (numeroInicial >= 0 && numeroFinal >= 0) {
        break;
      } else {
        System.out.println("Você digitou um numero negativo");
      }
    }

    for (int i = numeroInicial; i <= numeroFinal; i++) {
      String numString = Integer.toString(i);
      boolean ePalindromo = ePalindromo(numString);
      if (ePalindromo) {
        numPalindromo.add(numString);
      }
    }
    System.out.println("Numeros Palindromos : ");
    System.out.print(numPalindromo + " ");
  }

  private static boolean ePalindromo(String numString) {
    if (numString.length() == 1) {
      return true;
    } else {
      StringBuilder reverseString = new StringBuilder();
      for (int j = numString.length() - 1; j >= 0; j--) {
        reverseString.append(numString.charAt(j));
      }
      if (reverseString.toString().equals(numString)) {
        return true;
      }
      return false;
    }
  }
}
