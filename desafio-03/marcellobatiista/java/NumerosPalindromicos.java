import java.util.ArrayList;
import java.util.Scanner;

public class NumerosPalindromicos {

        public static void main(String[] args) {
        long max = 1 << 64 - 1L; max = -1 * max;

        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite um valor inicial: ");
        long numeroinicial = entrada.nextLong();
        System.out.print("Digite um valor final: ");
        long numerofinal = entrada.nextLong();

        int condicao = numeroinicial < 0 || numerofinal < 0 ? 0:1; 

        ArrayList<Long> palin = new ArrayList<Long>();

        for (; (numeroinicial <= numerofinal) && (numerofinal < max) && (condicao != 0); numeroinicial++) {
            if (ehPolindromo(numeroinicial)) {
                palin.add(numeroinicial);
                continue;
            }
            long soma = numeroinicial+inverso(numeroinicial);
            long polindromo = buscaPolindromo(soma);
        }

        if (palin.size() != 0) {
	    System.out.println("\nOs numeros palindromicos entre esse intervalo sao:\n");
	    for (Long long1 : palin) {
	        System.out.println(long1);
	    }
        } else if (condicao == 0) {
	    System.out.println("\nNao e possivel inserir numeros negativos...");
	} else {
	    System.out.println("\nO numero final ultrapassou o limite maximo de alcance: (1 << 64) - 1 (maximo unsigned int de 64 bits)...");
        }
    }

    static long inverso(long num) {
        String numero = Long.toString(num);
        int i = numero.length() - 1;
        String r = "";

        while (i >= 0) {
            r += numero.charAt(i);
            i--;
        }
        return Long.parseLong(r);
    }

    static boolean ehPolindromo(long num) {
        return num == inverso(num);
    }

    static long buscaPolindromo(long soma) {
        if (ehPolindromo(soma) == false) {
            try {
                buscaPolindromo(soma + inverso(soma));
            } catch(Exception e) {
                //Buscou tanto, que não encontrou
            }
        }
        return soma;
    }
}