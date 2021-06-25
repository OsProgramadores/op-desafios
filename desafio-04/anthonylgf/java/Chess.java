import java.util.Scanner;

public class Chess {
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in); //leitor

    int tabuleiro[][] = new int[8][8];// tabuleiro

    int i=0;
    int j=0;

    int numPeao = 0;
    int numRei = 0;
    int numDama = 0;
    int numBispo = 0;
    int numTorre = 0;
    int numCavalo = 0;

    /*Código para preencher tabuleiro*/
    for(i=0; i<8; i++){
      for(j=0; j<8; j++){
        tabuleiro[i][j] = in.nextInt();
      }
    }

    /*Somando num das peças usando operador ternário*/
    for(i=0; i<8; i++){
      for(j=0; j<8; j++){
        numCavalo = tabuleiro[i][j] == 3 ? ++numCavalo:numCavalo;
        numPeao = tabuleiro[i][j] == 1 ? ++numPeao:numPeao;
        numBispo = tabuleiro[i][j] == 2 ? ++numBispo:numBispo;
        numTorre = tabuleiro[i][j] == 4 ? ++numTorre:numTorre;
        numDama = tabuleiro[i][j] == 5 ? ++numCavalo:numDama;
        numRei = tabuleiro[i][j] == 6 ? ++numRei:numRei;
      }
    }

    System.out.println("Peao: " + numPeao + " peça(s)");
    System.out.println("Bispo: " + numBispo + " peça(s)");
    System.out.println("Cavalo: " + numCavalo + " peça(s)");
    System.out.println("Torre: " + numTorre + " peça(s)");
    System.out.println("Dama: " + numDama + " peça(s)");
    System.out.println("Rei: " + numRei + " peça(s)");
  }
}
