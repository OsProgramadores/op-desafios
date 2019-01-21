import java.util.Scanner;

public class Desafio04 {

    private static final String MENSAGEM = "%s: %d peça(s)";

    public static void main(final String[] args) {

        int pecas[] = new int[6];

        try (Scanner scanner = new Scanner(System.in)) {

            while (scanner.hasNextInt()) {

                final int peca = scanner.nextInt();
                if (peca >= 1 && peca <= 6) {
                    pecas[peca - 1]++;
                }

            }

        }

        System.out.println(String.format(MENSAGEM, "Peão", pecas[0]));
        System.out.println(String.format(MENSAGEM, "Bispo", pecas[1]));
        System.out.println(String.format(MENSAGEM, "Cavalo", pecas[2]));
        System.out.println(String.format(MENSAGEM, "Torre", pecas[3]));
        System.out.println(String.format(MENSAGEM, "Rainha", pecas[4]));
        System.out.println(String.format(MENSAGEM, "Rei", pecas[5]));

    }

}
