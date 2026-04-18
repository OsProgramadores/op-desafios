public class Desafio02 {
  public static void main(String[] args) {
    for (int i = 1; i < 10000; i++) {
      if (isPRIME(i)) {
        System.out.println(i);
      }
    }
  }

  private static boolean isPRIME(int n) {
    if (n <= 1)
      return false;
    if (n <= 3)
      return true;
    if (n % 2 == 0 || n % 3 == 0)
      return false;

    for (int i = 5; i * i <= n; i = i + 6) {
      if (n % i == 0 || n % (i + 2) == 0)
        return false;
    }
    return true;
  }
}
