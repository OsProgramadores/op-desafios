package java;

import java.util.Scanner;

public class Palindromo {
    public static boolean isPalidromo(long num) {
        String numStr = String.valueOf(num);
        StringBuilder strInverso = new StringBuilder(numStr).reverse();
        return numStr.equals(strInverso.toString());
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long inicial, fim;
        System.out.print("Escolha o numero inicial: ");
        inicial = scan.nextLong();
        System.out.print("Escolha o numero final: ");
        fim = scan.nextLong();
        if (inicial < 0 || fim < 0) {
            System.out.println("Não podem numeros negativos");
            scan.close();
            return;
        }

        if(inicial > fim) {
            System.out.println("O inicio não pode ser maior");
            scan.close();
            return;
        }

        for(long i = inicial; i <= fim; i++) {
            if(Palindromo.isPalidromo(i)) {
                System.out.println(i);
            }
        }
        scan.close();
    }
}
