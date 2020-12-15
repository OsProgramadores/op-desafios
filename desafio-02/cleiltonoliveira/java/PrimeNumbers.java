
public class PrimeNumbers {
	public static void main(String[] args) {
		int n = 10000;
		while (n > 1) {
			if (isPrime(n))
				System.out.println(n);
			n--;
		}
	}

	public static boolean isPrime(int number) {
		for (int i = 2; i < number; i++)
			if (number % i == 0)
				return false;
		return true;
	}
}
