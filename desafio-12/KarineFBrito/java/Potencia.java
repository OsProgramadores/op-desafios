import java.io.*;

public class Potencia{
    public static void main(String[] args){
        
        if (args.length != 1) {
          System.out.println(
              "Nenhum caminho foi fornecido,  execute o programa usando 'java Fracoes"
              + " <caminho-absoluto>'");
            return;
        }

        File caminho = new File(args[0]);
        if (!caminho.exists()) {
            System.out.println("Arquivo não encontrado.");
            return;
        }
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))){
            String linha; 
            while(linha = br.readLine != null){
                if(linha.trim().isEmpty()){
                    continue;
                }
            }


        } catch (IOException e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }

}