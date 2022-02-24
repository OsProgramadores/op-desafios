import java.util.Scanner;

public class PalindromicNumbers {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Integer inicio = sc.nextInt();
    Integer termino = sc.nextInt();
    for (Integer i = inicio; i <= termino; i++) {
      String str = i.toString();
      StringBuilder input = new StringBuilder();
      String reversedStr = input.append(str).reverse().toString();
      if (str.equals(reversedStr)) System.out.println(str);
    }
    sc.close();
  }
}
