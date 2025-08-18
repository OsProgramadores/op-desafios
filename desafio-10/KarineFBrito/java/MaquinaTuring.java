import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MaquinaTuring {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Nenhum caminho foi fornecido, execute o programa usando: ' java MaquinaTuring" + " <caminho-absoluto>'");
            return;
        }
        File caminho = new File(args[0]);
        if (!caminho.exists()) {
            System.out.println("Esse caminho não existe");
            return;
        }
        File pastaRegras = caminho.getParentFile();
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                linha = linha.trim();
                if (linha.isEmpty() || linha.startsWith(";")) continue;

                int posComentario = linha.indexOf(";");
                if (posComentario != -1) linha = linha.substring(0, posComentario).trim();

                String[] partes = linha.split(",", 2);
                if (partes.length < 2) {
                    System.err.println("Linha inválida (esperado 'arquivo,fitaEntrada'): " + linha);
                    continue;
                }

                String arquivoRegras = partes[0].trim();
                String fitaEntrada = partes[1].trim();

                File arquivoRegra = new File(pastaRegras, arquivoRegras);
                Map<String, Map<String, Regra>> regras = CarregaRegras(arquivoRegra.getAbsolutePath());

                Fita fita = new Fita(fitaEntrada);
                String saida = IniciarMaquina(regras, fita, "0");
                System.out.println(arquivoRegras + "," + fitaEntrada + "," + saida);
            }
        }catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Map<String, Map<String, Regra>> CarregaRegras(String ArquivoRegras) {
        Map<String, Map<String, Regra>> regras = new HashMap<>();
        try (BufferedReader br = new BufferedReader(new FileReader(ArquivoRegras))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                linha = linha.trim();
                if (linha.isEmpty() || linha.startsWith(";")) {
                    continue;
                }
                int posComentario = linha.indexOf(";");
                if (posComentario != -1) {
                    linha = linha.substring(0, posComentario);
                }
                if (linha.trim().isEmpty()) {
                    continue;
                }
                String limpa = linha.split(";", 2)[0].trim();
                String[] partes = limpa.split("\\s+");
                if (partes.length == 5) {
                    String estadoAtual = partes[0];
                    String simboloLido = partes[1];
                    String novoSimbolo = partes[2];
                    String direcao = partes[3];
                    String estadoNovo = partes[4];
                    Regra regra = new Regra(estadoAtual, simboloLido, novoSimbolo, direcao, estadoNovo);
                    regras.computeIfAbsent(estadoAtual, k -> new HashMap<>()).put(simboloLido, regra);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return regras;
    }

    public static Regra ProcurarRegra(Map<String, Map<String,Regra>> regras, String estadoAtual, char simboloLido) {
        Map<String, Regra> mapaEstado = regras.get(estadoAtual);
        if (mapaEstado != null) {
            Regra regra = mapaEstado.get(String.valueOf(simboloLido));
            if (regra != null) return regra;

            regra = mapaEstado.get("*");
            if (regra != null) return regra;
        }
        mapaEstado = regras.get("*");
        if (mapaEstado != null) {
            Regra regra = mapaEstado.get(String.valueOf(simboloLido));
            if (regra != null) return regra;
            regra = mapaEstado.get("*");
            if (regra != null) return regra;
        }
        return null;
    }

    public static String IniciarMaquina(Map<String, Map<String, Regra>> regras, Fita fita, String estadoAtual) {
        while (true) {
            char simboloLido = fita.ler();
            Regra regra = ProcurarRegra(regras, estadoAtual, simboloLido);

            if (regra == null ) {
                return "ERR";
            }

            String novoSimbolo = regra.novoSimbolo;
            String direcao = regra.direcao;
            String estadoNovo = regra.estadoNovo;

            if (!novoSimbolo.equals("*")) {
                fita.escrever(novoSimbolo.charAt(0));
            }
            fita.mover(direcao);
            estadoAtual = estadoNovo;
            if (estadoAtual.startsWith("halt")  || estadoAtual.equals("accept") || estadoAtual.equals("reject")) {
                break;
            }
        }
        return fita.toString();
    }
}


class Regra{
    String estadoAtual;
    String simboloLido;
    String novoSimbolo;
    String direcao;
    String estadoNovo;
    public Regra(String estadoAtual,String simboloLido,String novoSimbolo,String direcao,String estadoNovo) {
        this.estadoAtual = estadoAtual;
        this.simboloLido = simboloLido;
        this.novoSimbolo = novoSimbolo;
        this.direcao = direcao;
        this.estadoNovo = estadoNovo;
    }
    @Override
    public String toString() {
        return String.format("(%s, %s -> %s, %s, %s)", estadoAtual, simboloLido, novoSimbolo, direcao, estadoNovo);
    }
}
class Fita {
    List<Character> fita;
    int posicaoCabeca = 0;

    public Fita(String entrada) {
        fita = new ArrayList<>();
        for (char c : entrada.toCharArray()) {
            fita.add(c);
        }
    }

    public char ler() {
        return fita.get(posicaoCabeca);
    }

    public void escrever(char simbolo) {
        if (posicaoCabeca >= fita.size()) {
            fita.add(simbolo);
        } else {
            fita.set(posicaoCabeca, simbolo);
        }
    }

    public void mover(String direcao) {
        if (direcao.equals("r")) {
            posicaoCabeca++;
            if (posicaoCabeca >= fita.size()) {
                fita.add('_');
            }
        } else if (direcao.equals("l")) {
            posicaoCabeca--;
            if (posicaoCabeca < 0) {
                fita.add(0, '_');
                posicaoCabeca = 0;
            }
        }
        if (direcao.equals("*")) {
        }
    }
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (char c : fita) {
            sb.append(c);
        }
        return sb.toString();
    }
}