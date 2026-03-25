public class PrimeNumbers {
	public static void main(String[] args) {
		int start = 2;
		int end = 10000;
		int count = 0;

		for (int i = start; i <= end; i++) {
			for (int j = i; j >= 1; j--) {
				if (i % j == 0) {
					count++;
				}
			}
			if (count <= 2) {
				System.out.println(i);
			}
			count = 0;
		}
	}
}