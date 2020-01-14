import java.util.ArrayList;
import java.util.List;

public class PrimeNumbers {

	public static void main(String[] args) {
		int rangeStart = 1;
		int rangeEnd = 10000;
		
		//Initialize the list with the range to validate
		List<Integer> primeNummberList = new ArrayList<Integer>();
		for (int i = rangeStart; i <= rangeEnd; i++) {
			// Do not add 0 or 1, once we already know those values are not primes
			if (i > 1) {
				primeNummberList.add(i);
			}
		}
		
		//Using the Sieve of Eratosthenes method
		for (int i = rangeStart; i <= Math.sqrt(rangeEnd); i++) {
			if (isPrime(i)) {
				for (int j = i*2; j <= rangeEnd; j = j+i) {
					primeNummberList.remove(new Integer(j));
				}
			}
		}
		
		//Print the result: the list of prime numbers contained at the range calculated
		for (Integer primeNumber : primeNummberList) {
			System.out.println(primeNumber);
		}
	}
	
	public static boolean isPrime(int n) {
		int counter = 0;
		for (int i = 1; i <= n; i++) {
			if (n >= 2 && n % i == 0) {
				counter++;
			}
		}
		
		return counter > 0 && counter <= 2;
	}
}
