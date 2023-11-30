public class PrimeNumbers {
  public static void main(String[] args) {
    int firstNumber = 0;
    int lastNumber = 10000;

    int actualNumber = firstNumber;

    while (actualNumber <= lastNumber) {
      if (isPrimeNumber(actualNumber)) {
        System.out.println(actualNumber);
      }
      actualNumber++;
    }
  }

  static boolean isPrimeNumber(int number) {
    if (number <= 1) return false;

    for (int i = 2; i <= Math.sqrt(number); i++) if (number % i == 0) return false;

    return true;
  }
}
