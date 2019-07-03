
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class Xadrez {

    public static void main(String[] args) {
        class Peca {

            String nome;
            int quantidade;

            Peca(String nome) {
                this.nome = nome;
                this.quantidade = 0;
            }

            public void aumentar() {
                quantidade++;
            }

        }

        long start = System.currentTimeMillis();

        if (args.length != 1) {
            System.out.println("DIGITE: java -jar Xadrez.jar <arquivo>");

            return;
        }

        try {
            String[] tabuleiro = new String(Files.readAllBytes(Paths.get(args[0]))).replaceAll("\\r|\\n| ", "").split("");

            Map<String, Peca> pecas = new HashMap<String, Peca>();

            pecas.put("0", new Peca("Vazio"));
            pecas.put("1", new Peca("Peão"));
            pecas.put("2", new Peca("Bispo"));
            pecas.put("3", new Peca("Cavalo"));
            pecas.put("4", new Peca("Torre"));
            pecas.put("5", new Peca("Rainha"));
            pecas.put("6", new Peca("Rei"));

            for (String peca : tabuleiro) {
                pecas.get(peca).aumentar();

                pecas.replace(peca, pecas.get(peca));
            }

            pecas.remove("0");

            pecas.entrySet().forEach((peca) -> {
                System.out.println(((Peca) peca.getValue()).nome + ": " + ((Peca) peca.getValue()).quantidade + " peça(s)");
            });

        } catch (IOException e) {
            System.out.println("Falha ao ler o arquivo: " + args[0]);
        }

        System.out.println("Tempo total (milliseconds): " + (System.currentTimeMillis() - start));
    }
}
