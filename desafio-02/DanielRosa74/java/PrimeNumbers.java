import java.util.ArrayList;
import java.util.List;

public class PrimeNumbers {
  public static void main(String[] args) {
    List<Integer> primes = new ArrayList<>();
    primes.add(2);
    for (int i = 3; i <= 10000; i++) {
      int count = 0;
      for (int j = 1; j < i; j++) {
        if (i % j == 0) count++;
      }
      if (count < 2) primes.add(i);
    }
    System.out.print("Os números primos de 1 a 10000 são: ");
    for (int prime : primes) {
      System.out.print(prime + " ");
    }
  }
}
