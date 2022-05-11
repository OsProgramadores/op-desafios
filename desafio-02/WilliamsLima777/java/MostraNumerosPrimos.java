package numerosprimos;

public class MostraNumerosPrimos {

	public static void main(String[] args) {

		int numero = 1;
		System.out.println("2");
		System.out.println("3");
		System.out.println("5");

		for (int x = 1; x <= 10000; x++) {
			if (x > 1 &&  x % 2 != 0 && x % 3 != 0 && x % 5 !=0 && x % 7 != 0) {
				
				System.out.println(x);
			}
		}

	}

}
