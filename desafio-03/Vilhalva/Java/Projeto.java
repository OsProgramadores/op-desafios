public class Projeto {
    public static boolean ehPalindromo(int numero) {
        String numeroStr = Integer.toString(numero);
        int inicio = 0;
        int fim = numeroStr.length() - 1;

        while (inicio < fim) {
            if (numeroStr.charAt(inicio) != numeroStr.charAt(fim)) {
                return false;
            }
            inicio++;
            fim--;
        }
        return true;
    }

    public static void imprimirPalindromos(int inicio, int fim) {
        if (inicio < 1 || fim < 1 || inicio > fim) {
            System.out.println("ERRO: Entrada inválida! Certifique-se de que os limites são inteiros positivos.");
            return;
        }

        System.out.print("Números palíndromos entre " + inicio + " e " + fim + ": ");
        boolean primeiroPalindromoEncontrado = false;

        for (int i = inicio; i <= fim; i++) {
            if (ehPalindromo(i)) {
                if (primeiroPalindromoEncontrado) {
                    System.out.print(", ");
                }
                System.out.print(i);
                primeiroPalindromoEncontrado = true;
            }
        }

        System.out.println();
    }

    public static void main(String[] args) {
        imprimirPalindromos(1, 20);    
        imprimirPalindromos(3000, 3010); 
    }
}

