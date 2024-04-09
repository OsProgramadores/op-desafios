
public class PrimeNumbers {

	public static void main(String[] args) {
		// For para iterar entre 1 e 10000
		for (int i = 1; i <= 10000; i++) {
			if(isPrime(i)) {
				System.out.println(i);
			}

		}

	}

	//Função para verificar se o numero é primo
	public static boolean isPrime (int num) {
		//Se o numero for menor ou igual a 1 retornar false
		if (num <= 1) {
			return false;
		}

		for (int i = 2; i <= num / 2; i++) {
			if (num % i == 0) {
				return false;
			}

		}

	return true;
	}

}
