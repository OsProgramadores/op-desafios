import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Tac {
  public static void main(String[] args) {
    if (args.length != 1) {
      System.out.println("Nenhum caminho foi fornecido");
      return;
    }

    File caminho = new File(args[0]);
    if (!caminho.exists()) {
      System.out.println("Arquivo não encontrado.");
      return;
    }
    int tamanhoBuffer = 4096;
    try (RandomAccessFile aq = new RandomAccessFile(caminho, "r")) {
      long tamanhoRestante = aq.length();
      byte[] buffer = new byte[tamanhoBuffer];
      List<Byte> linha = new ArrayList<>();
      while (tamanhoRestante > 0) {
        int aLer = (int) Math.min(tamanhoBuffer, tamanhoRestante);
        tamanhoRestante -= aLer;
        aq.seek(tamanhoRestante);
        aq.readFully(buffer, 0, aLer);

        for (int i = aLer - 1; i >= 0; i--) {
          byte c = buffer[i];
          if (c == '\n') {
            if (linha.size() != 0) {
              imprimir(linha);
              linha.clear();
            }
            linha.add(c);
          } else {
            linha.add((byte) c);
          }
        }
      }
      if (!linha.isEmpty()) {
        imprimir(linha);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static void imprimir(List<Byte> linha) {
    Collections.reverse(linha);
    byte[] array = new byte[linha.size()];
    for (int j = 0; j < linha.size(); j++) {
      array[j] = linha.get(j);
    }
    System.out.print(new String(array, StandardCharsets.UTF_8));
  }
}
