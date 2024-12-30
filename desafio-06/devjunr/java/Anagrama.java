import java.util.List;
import java.util.Scanner;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Anagrama{
    public static void validaEntrada(String entrada){
        if (!entrada.replaceAll(" ", "").matches("[A-Z]+")) {
            System.out.println("> Entrada inválida. Digite apenas letras de A a Z, sem simbolos.");
            System.exit(1);
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a palavra ou expressão: ");
        String expressao = sc.nextLine();
        expressao = expressao.toUpperCase();
        validaEntrada(expressao);
        try{
            Path caminho = Paths.get("words.txt");
            List<String> palavras = Files.readAllLines(caminho);
            System.out.println(palavras);
        }catch(Exception e){
            System.out.println("> Erro ao ler o arquivo. " + e);
        }
    }
}