package anthony;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private static String sequence = "";

    public static void main(String[] args) {

        if (args.length != 1) {
            System.out.println("Digite java Main <nome-arquivo>");
            return;
        }

        int[] decimalFields = null;

        try (final Scanner scan = new Scanner(new File(args[0]))) {
            String decimalFieldsStr = scan.nextLine();
            final int indexPoint = decimalFieldsStr.indexOf('.');
            decimalFieldsStr = decimalFieldsStr.substring(indexPoint + 1);

            decimalFields = Arrays.stream(decimalFieldsStr.split(""))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        } catch (FileNotFoundException e) {
            throw new RuntimeException("Could not open file", e);
        }

        final int[] primeList = getPrimeList();

        printSequence(primeList, decimalFields);
    }

    private static void printSequence(final int[] primeList, final int[] decimalFields) {

        for (int startPoint = 0; startPoint < decimalFields.length; startPoint++) {
            getSequence(primeList, decimalFields, startPoint, new StringBuilder());
        }

        final String[] tokens = sequence.split(" ");
        Arrays.stream(tokens).forEach(System.out::print);
        System.out.println();
    }

    private static void getSequence(final int[] primeList,
                                    final int[] decimalFields,
                                    final int startPoint,
                                    final StringBuilder sb) {
        int numeroAtual = 0;
        final StringBuilder actualSeq = new StringBuilder();

        for (int i = startPoint; i < decimalFields.length; i++) {
            numeroAtual = numeroAtual * 10 + decimalFields[i];
            actualSeq.append(decimalFields[i]);

            if (numeroAtual > primeList[primeList.length - 1]) {
                break;
            } else if (Arrays.binarySearch(primeList, numeroAtual) >= 0) {
                final StringBuilder newSb = new StringBuilder(sb);
                newSb.append(" ");
                newSb.append(actualSeq);

                getSequence(primeList, decimalFields, i + 1, newSb);
            }
        }

        if (sb.length() >= sequence.length()) {
            sequence = sb.toString();
        }
    }

    private static int[] getPrimeList() {
        int size = 1;
        final int[] result = new int[9999];
        result[0] = 2;

        for (int i = 3; i <= 9973; i++) {
            boolean isPrime = true;

            for (int j = 0; j < size; j++) {
                if (i % result[j] == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                result[size++] = i;
        }

        return Arrays.copyOfRange(result, 0, size);
    }
}
