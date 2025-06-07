import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

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
      byte[] buffer = new byte[(int) tamanho];
      aq.readFully(buffer);
      List<Byte> linha = new ArrayList<>();
      for (int i = buffer.length - 1; i >= 0; i--) {
        byte c = buffer[i];
        if (c == '\n') {
          if (linha.size() != 0) {
            Collections.reverse(linha);
            byte[] array = new byte[linha.size()];

            for (int j = 0; j < linha.size(); j++) {
              array[j] = linha.get(j);
            }
            System.out.println(new String(array, StandardCharsets.UTF_8));
            linha.clear();
          }
        } else {
          linha.add((byte) c);
        }
      }
      if (!linha.isEmpty()) {
        Collections.reverse(linha);
        byte[] array = new byte[linha.size()];
        for (int j = 0; j < linha.size(); j++) {
          array[j] = linha.get(j);
        }
        System.out.println(new String(array, StandardCharsets.UTF_8));
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
