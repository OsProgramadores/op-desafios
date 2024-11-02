import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class anagrama {
  public static void main(String[] args) throws IOException {
    if (args.length == 0) {
      System.out.println("É necessário passar uma palavra como argumento na execução");
    } else {
      try {
        ArrayList<String> palavras = new ArrayList<>();
        for (String palavra : args) {
          palavra = palavra.toUpperCase();
          palavras.add(palavra);
        }
        String palavrasParaComparacao = String.join("", palavras);
        tratamentoDaEntrada(palavrasParaComparacao);
      } catch (Exception e) {
        System.out.println("Erro inesperado: " + e.getMessage());
      }
    }
  }

  public static void tratamentoDaEntrada(String palavraDoUsuario) throws IOException {
    if (palavraDoUsuario.length() > 16) {
      System.out.println("Apenas é possivel uma expressão de até 16 caracteres");
    } else if (!palavraDoUsuario.matches("[A-Z]+")) { // Validação da string
      System.out.println(
          "A palavra contém caracteres inválidos. Apenas letras de A a Z são permitidas.");
    } else {
      System.out.println("Palavra: " + palavraDoUsuario);
      System.out.println("_".repeat(10));
      System.out.println("Anagramas: ");
      AnagramaResultados(palavraDoUsuario);
    }
  }

  public static void AnagramaResultados(String filtragemAnagrama) throws IOException {
    try {
      File arquivo = new File("words.txt");
      Scanner scanner = new Scanner(arquivo);
      String palavraOrdenada = ordenarPalavra(filtragemAnagrama);

      while (scanner.hasNextLine()) {
        String linha = scanner.nextLine().toUpperCase();
        if (linha.length() == filtragemAnagrama.length()
            && ordenarPalavra(linha).equals(palavraOrdenada)) {
          System.out.println(linha);
        }
      }
      scanner.close();
    } catch (FileNotFoundException e) {
      System.out.println(
          "\n"
              + "ERRO: O arquivo com as palavras não foi encontrado\n"
              + "Guarde o arquivo words.txt no mesmo local do código java");
    }
  }

  private static String ordenarPalavra(String str) {
    char[] chars = str.toCharArray();
    Arrays.sort(chars);
    return new String(chars);
  }
}
