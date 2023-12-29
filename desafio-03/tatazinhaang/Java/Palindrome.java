package palindrome;

import java.util.Scanner;

public class Palindrome {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.println("Digite 2 valores inteiros e positivos: ");

		int valorInicial = sc.nextInt();
		int valorFinal = sc.nextInt();

		if (valorInicial < 0 || valorFinal < 0) {
			System.out.println("Os valores digitados devem ser inteiros e positivos");
		} else if (valorInicial > valorFinal) {
			System.out.println("O valor inicial deve ser menor que o valor final");
		} else {
			System.out.println(" Os números palindromos entre " + valorInicial + " e " + valorFinal + " são ");
			for (int i = valorInicial; i <= valorFinal; i++) {
				if (isPalindrome(i)) {
					System.out.println(i);
				}
			}
		}

		sc.close();
	}

	private static boolean isPalindrome(int number) {
		String strNumber = Integer.toString(number);
		String reversedStr = new StringBuilder(strNumber).reverse().toString();
		return strNumber.equals(reversedStr);
	}
}