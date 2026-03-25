import java.util.ArrayList;
import java.util.Collection;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class PalindromeNumbers {

    private static final int countDigits(long number) {
        return str(number).length();
    }

    private static final String str(long number) {
        return String.valueOf(number);
    }

    private static final String reverse(long number) {
        return new StringBuilder(str(number)).reverse()
            .toString();
    }

    private static final Collection<Long> generate(final long digits) {

        // Todo número de 0 a 9 é palíndromo
        if (digits == 1) {
            return LongStream.rangeClosed(0, 9)
                .boxed()
                .collect(Collectors.toList());
        }

        // Identifica os máximos e mínimos de acordo com a quantidade de dígitos
        // Exempĺo: O intervalo para um palíndromo de 4 dígitos será [10,100)
        long max = (long) Math.pow(10, digits / 2);
        long min = max / 10;

        if (digits % 2 == 0) {

            // Caso a quantidade de dígitos seja par, basta percorrer o intervalo concatenando o valor com o seu inverso
            // Exemplo: 21 irá virar 2112

            return LongStream.range(min, max)
                .map(l -> Long.valueOf(str(l) + reverse(l)))
                .boxed()
                .collect(Collectors.toList());

        }

        // Caso a quantidade de dígitos seja ímpar, há um passo adicional com uma iteração de 1 a 9
        // Exemplo: 21 irá virar 21012, 21112, 21312, ..., 21912
        Collection<Long> result = new ArrayList<>();
        for (long l = min; l < max; l++) {
            for (int i = 0; i < 10; i++) {
                long p = Long.valueOf(str(l) + i + reverse(l));
                result.add(p);
            }
        }

        return result;
    }

    private static final Collection<Long> generate(final long min, final long max) {

        int digitsMin = countDigits(min);
        int digitsMax = countDigits(max);

        Collection<Long> result = new ArrayList<>();
        for (int i = digitsMin; i <= digitsMax; i++) {

            // Gera todos os palíndromos com a quantidade de dígitos
            Collection<Long> temp = generate(i);

            // Remove valores menores que o mínimo
            if (i == digitsMin) {
                temp = temp.stream()
                    .filter(number -> number >= min)
                    .collect(Collectors.toList());
            }

            // Remove valores maiores que o máximo
            if (i == digitsMax) {
                temp = temp.stream()
                    .filter(number -> number <= max)
                    .collect(Collectors.toList());
            }

            result.addAll(temp);

        }

        return result;

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

        System.out.println(generate(min, max));

    }

}
