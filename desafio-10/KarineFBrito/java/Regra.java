public class Regra {
    int posicao;
    String estadoAtual;
    String simboloLido;
    String novoSimbolo;
    String direcao;
    String estadoNovo;

    public Regra(
            int posicao,
            String estadoAtual,
            String simboloLido,
            String novoSimbolo,
            String direcao,
            String estadoNovo) {
        this.posicao = posicao;
        this.estadoAtual = estadoAtual;
        this.simboloLido = simboloLido;
        this.novoSimbolo = novoSimbolo;
        this.direcao = direcao;
        this.estadoNovo = estadoNovo;
    }

    @Override
    public String toString() {
        return String.format(
                "(%s,%s, %s -> %s, %s, %s)",
                posicao, estadoAtual, simboloLido, novoSimbolo, direcao, estadoNovo);
    }
}
