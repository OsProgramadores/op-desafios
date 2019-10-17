package Desafio03;

import java.util.Scanner;

public class Palindrome {
	public static void main(String[] args) {
        long start = System.currentTimeMillis();

		int numberStart;
		int numberEnd;

		Scanner s = new Scanner(System.in);

		System.out.println("type 2 number to dicovery the palindromes betwee then");

		do {
			System.out.print("Start number: ");
			numberStart = s.nextInt();
			System.out.print("End number: ");
			numberEnd = s.nextInt();
			
		} while (numberStart > numberEnd || numberStart<0 || numberEnd<0);
		for (int i = numberStart; i <= numberEnd; i++) {
			if (i < 10) {
				System.out.println(i);
			} else {
				if (isPali(splitNumber(i))) {
					System.out.println(i);
				}
			}
		}
        System.out.println("total time (milliseconds): " + (System.currentTimeMillis() - start));

	}

	private static boolean isPali(int[] digits) {
		boolean pali = false;
		int end = digits.length;
		for (int i = 0, j = end-1; i < end/2; i++, j--) {
			if (digits[i] == digits[j]) {
				pali = true;
			} else {
				pali = false;
				break;
			}
		}
		return pali;
	}

	static int[] splitNumber(int number) {
		int digit;
		int aux;
		int[] digits;

		digit = String.valueOf(number).length();
		digits = new int[digit];

		for (int i = digit - 1; i >= 0; i--) {
			aux = number % 10;
			number /= 10;
			digits[i] = aux;
		}
		return digits;
	}
}
