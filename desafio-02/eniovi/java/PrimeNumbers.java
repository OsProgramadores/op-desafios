import java.util.ArrayList;
import java.util.List;

public class PrimeNumbers {

	private static List<Integer> primeNumber;


	public static void main(final String[] args) {
		primeNumber = new ArrayList<>();

		for (int i = 1; i < 10_000; i++) {
			if (isPrime(i)) {
				primeNumber.add(i);
			}
		}

		System.out.printf("Prime numbers between 1 and 10000\n%s\n\n", primeNumber);
		System.out.printf("Prime numbers total: %d\n", primeNumber.size());
	}


	public static boolean isPrime(final Integer number) {
		if (number == 1 || isEven(number) && number != 2) {
			return false;
		}

		if (number == 2) {
			return true;
		}

		return checkNumberWithPreviousPrimeNumberFound(number);
	}


	private static boolean checkNumberWithPreviousPrimeNumberFound(final Integer number) {
		for (final Integer prime : primeNumber) {
			if (number % prime == 0) {
				return false;
			}

			if (number / prime < prime && number % prime != 0) {
				return true;
			}
		}

		return false;
	}


	public static boolean isEven(final Integer number) {
		return number % 2 == 0;
	}

}
