

import java.util.Scanner;

public class Desafio3 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Comeco do intervalo: ");
        int beginning = input.nextInt();
        System.out.println("Fim do intervalo: ");
        int ending = input.nextInt();
        input.close();

        while (beginning <= ending) {
            if (isPalindrome(beginning)) {
                System.out.println(beginning);
            }
            beginning++;
        }
    }

    public static boolean isPalindrome(int number) {
        int aux = number;
        // Qualquer numero que tenha menos de 2 algarismos é palindromo
        if (number < 10){
            return true;
        }
        // Vamos inverter o número dado
        int reversedNumber = 0;
        while (aux != 0) {
            int lastDigit = aux % 10;
            reversedNumber = reversedNumber*10 + lastDigit;
            aux = aux / 10;
        }

        // Verificamos se ele é palindromo
        if (number == reversedNumber) {
            return true;
        } else {
            return false;
        }

    }



}