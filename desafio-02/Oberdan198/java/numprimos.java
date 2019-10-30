
public class numprimo {

	public static void main(String[] args) {

		int n;
		boolean ehPrimo;

		while (true) {
			n = 10000;
			if (n > 0) {
				for (int i = 2; i <= n; i++) {
					int cont = 2;
					ehPrimo = true;

					while (ehPrimo && cont < i) {
						if (i % cont == 0) {
							ehPrimo = false;
						} else {
							cont++;
						}

					}
					if (ehPrimo) {
						System.out.println(i);
					}
				}{
					break;
				}
			}
		}

	}
}
