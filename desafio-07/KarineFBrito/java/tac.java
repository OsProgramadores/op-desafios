import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class tac {
  public static void main(String[] args) {
    String caminho = System.getenv("CAMINHO");
    System.out.println(caminho);
    if (caminho == null) {
      System.out.println("O caminho do arquivo não foi definido");
      return;
    }
    Path c = Paths.get(caminho);
    try (BufferedReader reader = Files.newBufferedReader(c)) {
      Deque<String> linhas = new ArrayDeque<>();
      String linha;
      while ((linha = reader.readLine()) != null) {
        linhas.push(linha);
      }

      for (String l : linhas) {
        System.out.println(l);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
