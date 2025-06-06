import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class tac {
  public static void main(String[] args) {
    if (args.length == 0) {
      System.out.println("Nenhum caminho foi fornecido");
      return;
    }
    File caminho = new File(String.join(File.separator, args));
    if (!caminho.exists()) {
      System.out.println("Arquivo não encontrado.");
      return;
    }
    try (RandomAccessFile aq = new RandomAccessFile(caminho, "r")) {
      long tamanho = aq.length();
      StringBuilder linha = new StringBuilder();
      for (long i = tamanho - 1; i >= 0; i--) {
        aq.seek(i);
        int c = aq.read();
        if (c == '\n') {
          if(linha.length() != 0){
            System.out.println(linha.reverse().toString());
            linha.setLength(0);
          }  
        } else if (c != '\r') {
          linha.append((char) c);
        }
      }
      if (linha.length() > 0) {
        System.out.println(linha.reverse().toString());
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
