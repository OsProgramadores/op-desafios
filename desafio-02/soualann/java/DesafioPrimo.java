public class DesafioPrimo {
  public static void main(String[] args) {
    int num = 10000;

    for (int i = 2; i <= num; i++) {
      boolean primo = true;
      for (int j = 2; j < i; j++) {
        if (i % j == 0) {
          primo = false;
        }
      }
      if (primo) {
        System.out.println(i);
      }
    }
  }
}
