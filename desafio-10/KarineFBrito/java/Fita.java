import java.util.ArrayList;
import java.util.List;

public class Fita {
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
