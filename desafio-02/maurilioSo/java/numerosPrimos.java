
public class numerosPrimos {

	public static void main(String[] args) {

		/*
		 * Escreva um programa para listar todos os números primos entre 1 e 10000, na
		 * linguagem de sua preferência.
		 */

		int i = 2;

		while (i < 10000) {
			int teste = 0;

			for (int j = 2; j <= i / 2; j++) {

				if (i % j == 0) {
					teste++;
					break;
				}
			}

			if (teste == 0) {
				System.out.println(i);

			}
			i++;

		}

	}

}

