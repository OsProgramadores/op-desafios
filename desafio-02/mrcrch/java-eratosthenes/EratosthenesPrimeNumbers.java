import java.util.BitSet;
import java.util.Collection;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class EratosthenesPrimeNumbers {

    private static final Collection<Integer> generate(final int start, final int end) {

        final int max = (int) Math.sqrt(end);
        final BitSet table = new BitSet(end);

        // Preenchimento da tabela completa
        IntStream
            .rangeClosed(2, end)
            .forEach(table::set);

        // Marca os números compostos
        IntStream
            .rangeClosed(2, max)
            .flatMap(value -> IntStream.iterate(value * 2, n -> n + value).takeWhile(n -> n <= end))
            .forEach(i -> table.set(i, false));

        // Remove os números fora do intervalo
        IntStream
            .rangeClosed(2, start + 1)
            .forEach(i -> table.set(i, false));

        return table.stream().boxed().collect(Collectors.toList());
    }

    public static void main(final String[] args) {

        int min = 0;
        int max = 1000;

        if (args.length > 0) {

            if (args.length != 2) {
                throw new IllegalArgumentException(
                    "Quantidade de parâmetros inválida. São esperados 2 parâmetro (min/max)");
            }

            final String paramMin = args[0];
            final String paramMax = args[1];

            try {
                min = Integer.valueOf(paramMin);
            } catch (final NumberFormatException e) {
                throw new IllegalArgumentException("Parâmetro mínimo não é um número válido: " + paramMin);
            }

            try {
                max = Integer.valueOf(paramMax);
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

        final Collection<Integer> primes = generate(min, max);
        System.out.println(primes.stream()
            .map(String::valueOf)
            .collect(Collectors.joining(", ")));

    }

}
