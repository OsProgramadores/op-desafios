import java.util.*;

public class PalindromicNumbers {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    try {
      System.out.print("Insira o valor inicial: ");
      Integer inicio = sc.nextInt();
      System.out.print("Insira o valor final: ");
      Integer termino = sc.nextInt();
      if (inicio > termino || inicio < 0 || termino < 0) {
        System.out.println(
            "O valor de término precisa ser maior que o de início e ambos devem ser positivos."
                + "Tente novamente.");
        System.out.print("Insira o valor inicial: ");
        inicio = sc.nextInt();
        System.out.print("Insira o valor final: ");
        termino = sc.nextInt();
      }
      for (Integer i = inicio; i <= termino; i++) {
        String str = i.toString();
        StringBuilder input = new StringBuilder();
        String reversedStr = input.append(str).reverse().toString();
        if (str.equals(reversedStr)) System.out.println(str);
    } catch (InputMismatchException e) {
      System.out.println("Os limites de início e de término precisam ser números inteiros.");
    }
    sc.close();
  }
}
