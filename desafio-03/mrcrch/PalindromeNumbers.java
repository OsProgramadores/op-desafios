import java.util.Collection;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.stream.Collectors;

public class PalindromeNumbers {

    private static final int countDigits(long number) {
        return number == 0 ? 1 : (int) (Math.log10(number) + 1);
    }

    public static void main(final String[] args) {

        long min = 0;
        long max = 1000;

        if (args.length > 0) {

            if (args.length != 2) {
                throw new IllegalArgumentException(
                    "Quantidade de parâmetros inválida. São esperados 2 parâmetro (min/max)");
            }

            final String paramMin = args[0];
            final String paramMax = args[1];

            try {
                min = Long.valueOf(paramMin);
            } catch (final NumberFormatException e) {
                throw new IllegalArgumentException("Parâmetro mínimo não é um número válido: " + paramMin);
            }

            try {
                max = Long.valueOf(paramMax);
            } catch (final NumberFormatException e) {
                throw new IllegalArgumentException("Parâmetro máximo não é um número válido: " + paramMax);
            }

        }

        if (min < 0) {
            throw new IllegalArgumentException("Valor mínimo não pode ser negativo: " + min);
        }

        if (max < 0) {
            throw new IllegalArgumentException("Valor máximo não pode ser negativo: " + max);
        }

        if (max <= min) {
            throw new IllegalArgumentException("Valor máximo deve ser maior que o valor mínimo: " + min + "/" + max);
        }

        System.out.println(countDigits(min));
        System.out.println(countDigits(max));

    }

}
