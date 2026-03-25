import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
  enum LIMITS {
    LOWER(2),
    UPPER(10000);
    int number;

    private LIMITS(int number) {
      this.number = number;
    }
  }

  private static boolean isPrimeNumber(int number) {
    for (int i = LIMITS.LOWER.number; i * i <= number; i++) {
      if (number % i == 0) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out))) {
      for (int i = LIMITS.LOWER.number; i <= LIMITS.UPPER.number; i++) {
        if (isPrimeNumber(i)) {
          writer.write(String.valueOf(i));
          writer.newLine();
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
