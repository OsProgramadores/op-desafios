package teste;

public class desafio03 {


	public static void main(String[] args) {
		
		int resposta = 0;
		
		for(int i=1;i<=100000;i++) {
			int n = i;
			while(n > 0) {
				resposta += n % 10;
				resposta *= 10;
				n /= 10;
			}
			int numeroFinal = resposta/10;
			
			n = i;
			resposta = 0;
			
			if(n == numeroFinal) {
				System.out.println(n + " � pal�ndromo");
			} else {
				System.out.println(n + " n�o � pal�ndromo");
			}	
		}
	}
}
