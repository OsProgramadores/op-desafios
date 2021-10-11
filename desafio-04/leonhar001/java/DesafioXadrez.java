import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Function;
public class DesafioXadrez {

	public static void main(String[] args) {

		List<Integer> board = Arrays.asList(4,3,2,5,6,2,3,4,
				1,1,1,1,1,1,1,1,
				0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,
				1,1,1,1,1,1,1,1,
				4,3,2,5,6,2,3,4);

		List<String> piecesNames = Arrays.asList("Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei");
		List<Integer> piecesNumber = Arrays.asList(1,2,3,4,5,6);

		Function<Integer, String> count =
				s -> piecesNames.get(s-1)+": "+Collections.frequency(board, s)+" peça(s)";

		piecesNumber.stream()
			.map(count)
			.forEach(System.out::println);
	}
}
