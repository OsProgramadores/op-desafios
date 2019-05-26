public class Desafio2_v2{
	public static void main (String[] Args){
		int n;

		while(true){
			n = 10000;
			if (n>0){
				for (int i = 2; i <= n; i++){
					int contador = 2;
					boolean ehPrimo = true;
					while(ehPrimo && contador < i){
						if (i % contador == 0){
							ehPrimo = false;
						}
						else{
							contador++;
						}

					}

					if (ehPrimo){
						System.out.println(i);
					}
					
				}{
					break;
				}
			}
		}
	}

}
