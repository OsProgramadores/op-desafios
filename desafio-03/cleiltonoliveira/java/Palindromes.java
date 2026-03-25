public class Palindromes {
	public static void main(String[] args) {

		if (args.length != 2) {
			System.err.println("Informe o número iniciar e o final como paramentro");
			return;
		}
		try {
			long initialNumber = Integer.parseInt(args[0]);
			long finalNumber = Integer.parseInt(args[1]);
			palindrome(initialNumber, finalNumber);
		} catch (NumberFormatException e) {
			System.err.println("Insira apenas numeros inteiros positivos (máximo unsigned int de 64 bits)");
			return;
		}
	}

	private static void palindrome(long initialNumber, long finalNumber) {
		if (initialNumber < 0 || finalNumber < 0) {
			System.out.println("Os numeros devem ser inteiros positivos");
			return;
		} else if (initialNumber > finalNumber) {
			System.out.println("O número inicial deve ser menor que o final");
			return;
		}

		for (long i = initialNumber; i <= finalNumber; i++) {
			String newValue = new StringBuilder(i + "").reverse().toString();
			if (newValue.equals(i + ""))
				System.out.println(i);
		}
	}
}