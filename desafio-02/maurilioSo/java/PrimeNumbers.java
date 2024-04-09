
public class PrimeNumbers {

	public static void main(String[] args) {
		//O Programa gera uma lista com os numeros primos entre 1 e 10000.

		int num = 2, max = 10000;

		while(num < max) {
			int test = 0;
			for(int i = 2; i <= num / 2; i++) {
				if(num % i == 0) {
					test++;
					break;
				}

			}

			if(test == 0) {
				System.out.println(num);
			}

			num++;
		}

	}

}
