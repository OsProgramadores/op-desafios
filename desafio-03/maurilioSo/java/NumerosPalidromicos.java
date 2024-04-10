
public class NumerosPalidromicos {

	public static void main(String[] args) {

		for (int i = 1; i <= 100000; i++) {
			if (ehPalidromico(toString(i), i)) {
				System.out.println(i);
			}

		}

	}

	//Metodo para transformar o numero em String inverter a ordem do número
	public static String toString(int num_s) {
		String b = (num_s + "");
		String d = "";

		for (int i = b.length() - 1; i >= 0; i--) {
			d += b.charAt(i);
		}

		return d;

	}

	//Metodo para verificar se é Palidromico
	public static boolean ehPalidromico(String a, int num) {
		String b = (num + "");
		if (a.contentEquals(b)) {
			return true;
		}

		return false;

	}

}
