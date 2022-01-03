package net.marcorocha.osprogramadores.desafio05;

public class Principal { // NO_UCD (unused code)

    private Principal() {
    }

    public static void main(String... args) {

        if (args.length == 0) {
            System.err.println("Caminho para o arquivo não informado");
            System.exit(1);
        }

        new Desafio().resolver(args[0]);

    }

}
