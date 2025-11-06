import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Palindromos {

    int intervaloInicial;
    int intervaloFinal;
    List<Integer> palindromos;

    public Palindromos(int intervaloInicial, int intervaloFinal) {
        if (intervaloInicial <= 0) {
            throw new IllegalArgumentException(
                    "O valor inicial deve ser um número inteiro positivo (maior que 0).");
        }

        if (intervaloFinal <= 0) {
            throw new IllegalArgumentException(
                    "O valor final deve ser um número inteiro positivo (maior que 0).");
        }

        if (intervaloInicial > intervaloFinal) {
            throw new IllegalArgumentException(
                    "O valor inicial ("
                            + intervaloInicial
                            + ") não pode ser maior que o valor final ("
                            + intervaloFinal
                            + ").");
        }

        this.intervaloInicial = intervaloInicial;
        this.intervaloFinal = intervaloFinal;
        this.palindromos = encontrarPalindromos(intervaloInicial, intervaloFinal);
    }

    public static int lerInteiroPositivoMaiorQueOMinimo(String mensagem, int valorMinimo) {
        Scanner scanner = new Scanner(System.in);
        int numeroLido = 0;
        boolean entradaValida = false;

        while (!entradaValida) {
            System.out.print(mensagem);
            try {

                if (scanner.hasNextInt()) {
                    numeroLido = scanner.nextInt();

                    if (numeroLido > 0) {
                        if (numeroLido >= valorMinimo) {
                            entradaValida = true;
                        } else {
                            System.err.println(
                                    "Erro: O número deve ser um maior que o intervalo inicial. Tente novamente.");
                        }
                    } else {
                        System.err.println(
                                "Erro: O número deve ser um inteiro positivo (maior que zero). Tente novamente.");
                    }
                } else {
                    System.err.println("Erro: Entrada inválida. Por favor, digite um número inteiro.");
                    scanner.next();
                }

            } catch (InputMismatchException e) {
                System.err.println("Erro inesperado durante a leitura. Tente novamente.");
                scanner.nextLine(); // Limpa o buffer
            }
        }
        scanner.nextLine();
        return numeroLido;
    }

    private boolean isPalindromo(int numeroAReverter) {
        int original = numeroAReverter;
        int numeroRevertido = 0;
        while (numeroAReverter != 0) {
            int ultimoDigito = numeroAReverter % 10; // Pega o último dígito
            numeroRevertido = numeroRevertido * 10 + ultimoDigito; // Adiciona ao número reverso
            numeroAReverter /= 10; // Remove o último dígito
        }
        return original == numeroRevertido;
    }

    List<Integer> encontrarPalindromos(int intervaloInicial, int intervaloFinal) {
        palindromos = new ArrayList<>();
        for (int i = intervaloInicial; i <= intervaloFinal; i++) {
            if (i < 10) {
                palindromos.add(i);
            } else if (isPalindromo(i)) {
                palindromos.add(i);
            }
        }

        return palindromos;
    }

    @java.lang.Override
    public java.lang.String toString() {

        String resultadoFormatado =
                String.join(", ", palindromos.stream().map(Object::toString).toList());

        return resultadoFormatado;
    }

    public static void main(String[] args) {
        System.out.println();
        System.out.println("-------------- Desafio 03 - Os programadores --------------");
        System.out.println("Encontrar números palindrômicos entre dois outros números");
        System.out.println("-----------------------------------------------------------\n");
        int intervaloInicial =
                lerInteiroPositivoMaiorQueOMinimo(
                        "Informe um número inteiro positivo como intervalo inicial: ", 1);
        int intervaloFinal =
                lerInteiroPositivoMaiorQueOMinimo(
                        "Informe um número inteiro positivo maior ou igual a "
                                + intervaloInicial
                                + " como intervalo final: ",
                        intervaloInicial);
        Palindromos palindromos = new Palindromos(intervaloInicial, intervaloFinal);
        System.out.println(palindromos);
    }
}
