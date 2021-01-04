public class Xadrez {
    public static void main(String[] args) {
        String tab = 
                    "4 3 2 5 6 2 3 4"+
                    "1 1 1 1 1 1 1 1"+
                    "0 0 0 0 0 0 0 0"+
                    "0 0 0 0 0 0 0 0"+
                    "0 0 0 0 0 0 0 0"+
                    "0 0 0 0 0 0 0 0"+
                    "1 1 1 1 1 1 1 1"+
                    "4 3 2 5 6 2 3 4";

        String tipo[] = {"vazio" ,"Peao", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"};
        // pecas = {vazio, peao, bispo, cavalo, torre, rainha, rei}
        int quant[] = {0, 0, 0, 0, 0, 0, 0};

        int i = 0;
        while (i <= tab.length() - 1) {
            for (int peca = 1; peca < quant.length; peca++) {
                while (tab.charAt(i) == Integer.toString(peca).charAt(0)) {
                    quant[peca]++;
                    break;
                }
            }
            i++;
        }

        for (int j = 1; j < quant.length; j++) {
            System.out.println(tipo[j]+": "+quant[j]+" peças(s)");
        }
    }
}
