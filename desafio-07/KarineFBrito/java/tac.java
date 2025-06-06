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
      List <Byte> linha = new ArrayList<>();
      for (long i = tamanho - 1; i >= 0; i--) {
        aq.seek(i);
        int c = aq.read();
        if (c == '\n') {
          if(linha.size() != 0){
            Collections.reverse(linha);
            byte[] array = new byte[linha.size()];

            for (int j = 0; j < linha.size(); j++) {
              array[j] = linha.get(j);
            }

            System.out.print(new String(array, StandardCharsets.UTF_8));
            linha.clear();
          }
                     linha.add((byte) c);
 
          
        } else{
          linha.add((byte) c);
        } 
      } 
      if (linha.size() > 0) {
        byte[] array = new byte[linha.size()];
        Collections.reverse(linha);
        for (int j = 0; j < linha.size(); j++) {
              array[j] = linha.get(j);
        }
        System.out.print(new String(array, StandardCharsets.UTF_8));
      }

    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
