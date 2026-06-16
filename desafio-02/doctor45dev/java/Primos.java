public class Primos {
  public static boolean ehPrimo(int numero) {
    if (numero <= 1) {
      return false;
    }

    for (int i = 2; i * i <= numero; i++) {
      if (numero % i == 0) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    for (int i = 1; i <= 10000; i++) {
      if (ehPrimo(i)) {
        System.out.println(i);
      }
    }
  }
}
