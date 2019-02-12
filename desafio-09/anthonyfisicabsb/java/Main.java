import java.math.BigInteger;
import java.util.Scanner;
import java.io.File;

public class Main {

    private static BigInteger limit = new BigInteger("0");

    public static void main(String[] args) {
        Scanner sc = null;

        try {
            sc = new Scanner(new File(args[0]));
        } catch (Exception e) {
            System.out.println("Falha na leitura do arquivo!");
            System.out.println("Digite java Main <arquivo>");
            System.exit(-1);
        }

        limit = convertToTen("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", new BigInteger("62"));

        while (sc.hasNextLine()) {
            convertLine(sc.nextLine());
        }

        sc.close();
    }

    public static void convertLine(String lin) {
        String toks[] = lin.split(" ");

        BigInteger basOrg = new BigInteger(toks[0]);
        BigInteger basDes = new BigInteger(toks[1]);

        if (basOrg.intValue() > 62 || basOrg.intValue() < 2 || basDes.intValue() > 62 || basDes.intValue() < 2) {
            System.out.println("???");
            return;
        }

        BigInteger numConv = new BigInteger("0");

        numConv = convertToTen(toks[2], basOrg);

        if (numConv.intValue() == -1 || numConv.compareTo(limit) > 0) {
            System.out.println("???");
            return;
        }


        if (basDes.intValue() != 10) {
            convFromTen(numConv, basDes);
            return;
        }

        System.out.println(numConv.toString());
    }

    public static BigInteger convertToTen(String str, BigInteger base) {
        BigInteger retorno = new BigInteger("0");

        for (int i = str.length() - 1; i >= 0; i--) {
            int aux = str.charAt(i);

            if (aux < 58 && aux > 47)
                aux -= 48;
            else if (aux < 91 && aux > 64)
                aux -= 55;
            else if (aux < 123 && aux > 96)
                aux -= 61;
            else
                return new BigInteger("-1");

            if (aux >= base.intValue())
                return new BigInteger("-1");

            BigInteger temp = BigInteger.valueOf(aux);
            temp = temp.multiply(base.pow(str.length() - (1 + i)));

            retorno = retorno.add(temp);
        }

        return retorno;
    }

    public static void convFromTen(BigInteger num, BigInteger basDes) {
        StringBuilder sb = new StringBuilder();

        while (num.compareTo(basDes) >= 0) {
            BigInteger res = num.remainder(basDes);
            int aux = res.intValue();

            addDigit(aux, sb);
            num = num.divide(basDes);
        }

        addDigit(num.intValue(), sb);
        System.out.println(sb.toString());
    }

    public static void addDigit(int aux, StringBuilder sb) {
        if (aux < 10) {
            sb.insert(0, aux);
        } else if (aux < 36) {
            char ch = (char)(aux + 55);
            sb.insert(0, ch);
        } else {
            char ch = (char)(aux + 61);
            sb.insert(0, ch);
        }
    }
}

