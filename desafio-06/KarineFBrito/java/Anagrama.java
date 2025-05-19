import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class Anagrama {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Digite a expressão (somente letras e espaços): ");
    String entrada = scanner.nextLine().toUpperCase().replaceAll(" ", "");
    scanner.close();

    if (!entrada.matches("[A-Z]+")) {
      System.out.println("Expressão inválida! Apenas letras são permitidas.");
      return;
    }

    ArrayList<String> palavrasValidas = new ArrayList<>();
    try (Scanner arquivoScanner = new Scanner(new File("C:\\Users\\Karin\\Downloads\\words.txt"))) {
      while (arquivoScanner.hasNextLine()) {
        String palavra = arquivoScanner.nextLine().trim().toUpperCase();
        if (!palavra.isEmpty()) {
          palavrasValidas.add(palavra);
        }
      }
    } catch (FileNotFoundException e) {
      System.out.println("Arquivo words.txt não encontrado!");
      return;
    }

    if (palavrasValidas.isEmpty()) {
      System.out.println("Erro: Nenhuma palavra válida encontrada no arquivo.");
      return;
    }

    TreeSet<String> anagramas = new TreeSet<>();

    permutar(entrada, 0, entrada.length() - 1, palavrasValidas, anagramas);

    if (anagramas.isEmpty()) {
      System.out.println("Nenhum anagrama válido encontrado.");
    } else {
      for (String anagrama : anagramas) {
        System.out.println(anagrama);
      }
    }
  }

  private static void permutar(
      String str,
      int esquerda,
      int direita,
      ArrayList<String> palavrasValidas,
      TreeSet<String> anagramas) {
    if (esquerda == direita) {
      if (palavrasValidas.contains(str)) {
        anagramas.add(str);
      }
    } else {
      for (int i = esquerda; i <= direita; i++) {
        str = trocarPosicao(str, esquerda, i);
        permutar(str, esquerda + 1, direita, palavrasValidas, anagramas);
        str = trocarPosicao(str, esquerda, i);
      }
    }
  }

  public static String trocarPosicao(String palavra, int i, int j) {
    char[] letras = palavra.toCharArray();
    char temp = letras[i];
    letras[i] = letras[j];
    letras[j] = temp;
    return new String(letras);
  }
}
