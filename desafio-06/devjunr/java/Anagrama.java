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

    public static void lerPalavrasValidas(){
        try {
            Path caminho = Paths.get("words.txt");
            List<String> linhas = Files.readAllLines(caminho);
            System.out.println(linhas);
        } catch (java.nio.file.NoSuchFileException e) {
            System.out.println("Erro: Não foi possivel encontrar o arquivo words.txt");
        } catch (Exception e){
            System.out.println("Erro: " + e);
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a palavra ou expressão: ");
        String expressao = sc.nextLine();
        expressao = expressao.toUpperCase();
        lerPalavrasValidas();
        validaEntrada(expressao);
    }
}