public class Numeros {
	public static void main(String[] args) {
	        int limite = 10000;
	        boolean[] numerosPrimos = new boolean[limite + 1];
	        
	        for (int i = 2; i <= limite; i++) {
	            numerosPrimos[i] = true;
	        }

	        for (int i = 2; i * i <= limite; i++) {
	            if (numerosPrimos[i]) {
	                for (int j = i * i; j <= limite; j += i) {
	                    numerosPrimos[j] = false;
	                }
	            }
	        }

	        System.out.println("NÚMEROS PRIMOS ENTRE 1 e 10000:");
	        for (int i = 2; i <= limite; i++) {
	            if (numerosPrimos[i]) {
	                System.out.println("😳"+i + " ");
	            }
	        }
		}
}
