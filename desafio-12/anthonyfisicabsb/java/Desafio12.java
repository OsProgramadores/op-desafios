import java.io.File;
import java.util.Scanner;
import java.math.BigInteger;

public class Desafio12 {
	private static final BigInteger MINUS_ONE = new BigInteger("-1");

	public static void main(String args[]){
		if(args.length != 1){
			System.out.println("Digite java Desafio12 <nome-arquivo>");
			return;
		}

		final var arquivo = new File(args[0]);

		try(final var sc = new Scanner(arquivo)){
			while(sc.hasNext()){
				final String stringNum = sc.next();

				final BigInteger exponent = getExpoent(stringNum);

				if(exponent.equals(MINUS_ONE)){
					System.out.printf("%s false\n", stringNum);
				}else{
					System.out.printf("%s true %s\n", stringNum, exponent.toString());
				}
			}
		}catch(final Exception e){
			e.printStackTrace();
			System.out.println("Exception while trying to find exponent!");
		}
	}

	private static BigInteger getExpoent(final String num){
		BigInteger actualNum = new BigInteger(num);
		final BigInteger TWO = new BigInteger("2");
		
		if(actualNum.max(BigInteger.ZERO).equals(BigInteger.ZERO)){
			return MINUS_ONE;
		}

		BigInteger expoent = BigInteger.ZERO;
	
		while(actualNum.mod(TWO).intValue() == 0){
			actualNum = actualNum.shiftRight(1);
			expoent = expoent.add(BigInteger.ONE);
		}

		if(actualNum.equals(BigInteger.ONE)){
			return expoent;
		}

		return MINUS_ONE;
	}
}