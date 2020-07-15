package desafio3;


import java.util.InputMismatchException;
import java.util.Scanner;


public class polindromos {

	public static void main(String[] args) {
		
			
		Scanner teclado = new Scanner(System.in);
				
		System.out.println("Informe 2 numeros inteiros e positivos: ");
			
			try {
				 Long num1 = teclado.nextLong();
				 Long num2 = teclado.nextLong();
				 
				 if(num1 < 0 || num2 < 0) {
					 System.out.println("Você deve informar 2 números inteiros positivos!");
					 
					 } else if (num1 > num2) {
						 System.out.println("O primeiro número deve ser menor que o segundo número!");
						 } else {
						 
								 System.out.println("Os polindrômicos do intervalo entre "+num1+" e "+num2+ " : ");
								 
								 for(Long i = num1; i <= num2; i++) {
									 
									 String reverso = new StringBuilder( i + "").reverse().toString();
									 
									 	if(reverso.equals(i + "")) {
									 		System.out.println(i);
									 	}
								  }
						 	}
				} catch (InputMismatchException e) {
					System.out.println("Os números devem ser inteiros, com no maximo 64 bits!");
					
				}
			 
			 teclado.close();
		}			
	}

