
import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class PotenciasDe2 {

    private static final BigInteger TWO = new BigInteger("2");

    // https://stackoverflow.com/questions/739532/logarithm-of-a-bigdecimal
    public static double log(BigInteger val) {
        // Get the minimum number of bits necessary to hold this value.
        int n = val.bitLength();

        // Calculate the double-precision fraction of this number; as if the
        // binary point was left of the most significant '1' bit.
        // (Get the most significant 53 bits and divide by 2^53)
        long mask = 1L << 52; // mantissa is 53 bits (including hidden bit)
        long mantissa = 0;
        int j = 0;
        for (int i = 1; i < 54; i++) {
            j = n - i;
            if (j < 0) {
                break;
            }

            if (val.testBit(j)) {
                mantissa |= mask;
            }
            mask >>>= 1;
        }
        // Round up if next bit is 1.
        if (j > 0 && val.testBit(j - 1)) {
            mantissa++;
        }

        double f = mantissa / (double) (1L << 52);

        // Add the logarithm to the number of bits, and subtract 1 because the
        // number of bits is always higher than necessary for a number
        // (ie. log2(val)<n for every val).
        return (n - 1 + Math.log(f) * 1.44269504088896340735992468100189213742664595415298D);
        // Magic number converts from base e to base 2 before adding. For other
        // bases, correct the result, NOT this number!
    }

    private static void getPotenciaDeDois(String numero) {
        double potencia = log(new BigInteger(numero)) / log(TWO);

        if ((int) potencia >= 0 && potencia == Math.rint(potencia)) {
            System.out.println(numero + " true " + (int) potencia);
        } else {
            System.out.println(numero + " false");
        }
    }

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        if (args.length != 1) {
            System.out.println("DIGITE: java -jar PotenciasDe2.jar <arquivo>");

            return;
        }

        try (Stream<String> stream = Files.lines(Paths.get(args[0]))) {
            stream.forEach(numero -> getPotenciaDeDois(numero));
        } catch (IOException e) {
            System.out.println("Falha ao ler o arquivo: " + args[0]);
        }

        System.out.println("Tempo total (milliseconds): " + (System.currentTimeMillis() - start));
    }
}
