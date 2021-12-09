// desafio-02
public class Main {
  public static void main(String[] args) {
    for (int i = 1; i <= 10000; i++) {
      int counter = 0;
      for (int j = 1; j <= i; j++) {
        if (i % j == 0) {
          ++counter;
        }
      }
      if (counter == 2) {
        System.out.println(i);
      }
    }
  }
}
