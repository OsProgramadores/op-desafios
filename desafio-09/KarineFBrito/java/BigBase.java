import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.math.BigInteger;

public class BigBase {
    static final String digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"; //Determino os numeros possiveis
    static final int Base_Min = 2; // Determino a base minima
    static final int Base_Max = 62; // Determino a base maxima
    static final String Limite = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"; //determino o Limite
    public static void main(String[] args) {
        if (args.length != 1) { // Verifico se possui um caminho dado pelo o usuario
            System.out.println("Nenhum caminho foi fornecido,  execute o programa usando 'java bigbase <caminho-absoluto>'");
            return;
        }
        File caminho = new File(args[0]);
        if (!caminho.exists()) { //Verifico se o caminho passado existe
            System.out.println("Arquivo não encontrado.");
            return;
        }
        try (RandomAccessFile aq = new RandomAccessFile(caminho, "r")) {
            String linha;
            BigInteger limiteMax = converter(Limite, 62); // Transforma a string limite em um numero decimal

            while ((linha = aq.readLine()) != null) { // Verifico se a linha não está vazia, se não estiver ele continua rodando;
                String[] partes = linha.split(" ");
                if (partes.length != 3) { // Divido a linha em três partes Base_Entrada, Base_Saída e Numero
                    System.out.println("???");
                    continue;
                }
                int Base_Entrada = Integer.parseInt(partes[0]);
                int Base_Saida = Integer.parseInt(partes[1]);
                String numero = partes[2];
                if ( negativo (numero) || Base_Entrada < Base_Min || Base_Entrada > Base_Max || Base_Saida < Base_Min || Base_Saida > Base_Max) { //Verifico se o numero e negativo e se as bases se estão maior ou menor do permitido
                    System.out.println("???");
                    continue;
                }
                BigInteger decimal = converter(numero, Base_Entrada); //Converto para a base 10
                if(decimal == null ||  decimal.compareTo(limiteMax) > 0 ){ // Verifico se o numero decimal não e nulo e verifico se está no limite
                    System.out.println("???");
                    continue;
                }
                String converterBaseSaida = paraBase(decimal, Base_Saida); // Converto o numero decimal para a Base_Saída
                System.out.println(converterBaseSaida); //Imprimo o resultado
            }
        } catch (IOException e) { //Essa parte e responsavel para verificar os rastros do erro
             e.printStackTrace();
        }
    }

    static boolean negativo(String numero) { // Uso esse método para verificar se o numero e negativo
        return numero.startsWith("-"); //verifica se o numero inicia com o sinal negativo (-)
    }

    public static BigInteger converter(String numero, int Base_Entrada) { // Uso esse método para converter os numeros com a Base_Entrada para base decimal(10)
        BigInteger resultado = BigInteger.ZERO;
        BigInteger base = BigInteger.valueOf(Base_Entrada); ///base recebe o valor de Base_Entrada
        for (int i = 0; i <  numero.length(); i++) { // enquanto i for menor que o tamanho do numero, o laço vai rodar
            char c = numero.charAt(i); // Pega um caracter por vez do numero
            int valor = Valor_Digito(c);
            if (valor < 0 || valor >= Base_Entrada) { // verifica se o Digito e valido
                return null;
            }
            resultado = resultado.multiply(base).add(BigInteger.valueOf(valor)); // Faz o calculo: resultado = resultado*Base_Entrada + digito
        }
        return resultado; // retorna o resultado
    }
    public static String paraBase(BigInteger numero, int base) {
        if (numero.equals(BigInteger.ZERO)) { //verifico se o numero e = zero
             return "0";
        }
        StringBuilder resultado = new StringBuilder();
        BigInteger baseBig = BigInteger.valueOf(base);
        while (numero.compareTo(BigInteger.ZERO) > 0) { // Verifico se o numero e maior que zero(0)
            BigInteger[] divmod = numero.divideAndRemainder(baseBig); // Aqui estou fazendo o calculo da divisao completa e retornando o quociente e o resto
            int resto = divmod[1].intValue(); //Aqui estou pegando o resto da divisão e salvando no resto do tipo inteiro
            resultado.append(digitos.charAt(resto)); //Estou convertendo o resultado(resto da divisao) para uma base textual
            numero = divmod[0]; //Atualiza o valor do numero para o quociente da divisão
        }
        return resultado.reverse().toString();
    }

    public static int Valor_Digito(char c) { //converte um caracter em valor um valor numerico
        if (c >= '0' && c <= '9') {
            return c - '0';
        }
        if (c >= 'A' && c <= 'Z') {
            return c - 'A' + 10;
        }
        if (c >= 'a' && c <= 'z') {
            return c - 'a' + 36;
        }
        return -1;
    }
}