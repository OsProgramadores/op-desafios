public class Chess {
	public static void main(String[] args) {
		int board[] = { 4, 3, 2, 6, 5, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 2, 5, 6, 2, 3, 4 };

		int countKing = 0;
		int countQueen = 0;
		int countRook = 0;
		int countBishop = 0;
		int countKnight = 0;
		int countPawn = 0;

		for (int i : board) {
			countKing += i == 6 ? 1 : 0;
			countQueen += i == 5 ? 1 : 0;
			countRook += i == 4 ? 1 : 0;
			countBishop += i == 2 ? 1 : 0;
			countKnight += i == 3 ? 1 : 0;
			countPawn += i == 1 ? 1 : 0;
		}

		System.out.println("Número de Reis: " + countKing);
		System.out.println("Número de Damas: " + countQueen);
		System.out.println("Número de Torres: " + countRook);
		System.out.println("Número de Bispos: " + countBishop);
		System.out.println("Número de Cavalos: " + countKnight);
		System.out.println("Número de Peões: " + countPawn);
	}
}
