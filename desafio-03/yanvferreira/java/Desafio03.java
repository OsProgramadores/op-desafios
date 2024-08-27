import java.util.ArrayList;

public class Desafio03 {
    public static void main(String[] args) {
        int numeroInicial = 1;
        int numeroFinal = 20;

        System.out.println("Números Palíndromicos: " + verificaPalindromicos(numeroInicial, numeroFinal));;
    }

    private static ArrayList<String> verificaPalindromicos(int numeroInicial, int numeroFinal) {
        ArrayList<String> palindromico = new ArrayList<String>(); //Array para armazenar os números palindromicos

        while (numeroInicial <= numeroFinal) {
            if (numeroInicial < 10) { // por regra, de 1 a 9 são palindromicos
                palindromico.add(Integer.toString(numeroInicial));
                numeroInicial++;
                continue;
            }

            if (reverteNumero(numeroInicial)){
                palindromico.add(Integer.toString(numeroInicial));
            }

            numeroInicial++;
        }

        return palindromico;
    }

    private static boolean reverteNumero(int numeroInicial) {
        String numeroInvertido = "";

        //converte em array de String
        String numeroInicialString = Integer.toString(numeroInicial);

        // inverte as posições dos números
        for (int x = 0; x < numeroInicialString.length(); x++){
            numeroInvertido = numeroInicialString.charAt(x) + numeroInvertido;
        }

        // se o numeroInvertido for igual ao array de String do NumeroInicial, então adiciona no Arraylist Palindromico
        if (numeroInvertido.equals(numeroInicialString)) {
            return true;
        }

        return false;
    }
}