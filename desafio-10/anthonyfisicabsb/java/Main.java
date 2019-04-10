import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {

    private static boolean END_FLAG = false;
    private static boolean ABORTED = false;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Digite java Main <nome-arquivo>");
            return;
        }

        try (final Scanner sc = new Scanner(new File(args[0]))) {
            while (sc.hasNextLine()) {
                final String[] lineArray = sc.nextLine().split(",");

                final List<String[]> rules = getParams(lineArray[0]);

                final ArrayList<String> fitas = new ArrayList<>(Arrays.asList(lineArray[1].split("")));
                execute(fitas, rules);

                final StringBuilder response = new StringBuilder();

                fitas.forEach(ch -> response.append(ch));
                
                final String responseStr = response.toString().trim();

                System.out.print(lineArray[0] + ",");
                System.out.print(lineArray[1] + ",");
                System.out.println(responseStr);
            }

        } catch (FileNotFoundException e) {
            throw new RuntimeException("Could not open file!", e);
        }
    }

    private static void execute(final List<String> fitas, final List<String[]> params){
        final StringBuilder currentState = new StringBuilder("0");
        final StringBuilder newSimbol = new StringBuilder();

        int pos = 0;

        while (!END_FLAG){
            setString(newSimbol, fitas.get(pos));
            final byte posIncr = getPosIncr(currentState, newSimbol, params);

            if(newSimbol.toString().equals("_")){
                newSimbol.delete(0, newSimbol.length());
                newSimbol.append(" ");
            }

            if(ABORTED){
                fitas.clear();
                fitas.add("ERR");
                break;
            }

            if(pos + posIncr < 0){
                fitas.set(pos, newSimbol.toString());
                fitas.add(0, " ");
            }else {
                if(pos + posIncr == fitas.size()) {
                    fitas.add(" ");
                }

                fitas.set(pos, newSimbol.toString());
                pos += posIncr;
            }
        }

        END_FLAG = false;
        ABORTED = false;
    }

    private static byte getPosIncr(final StringBuilder currentState, final StringBuilder newSimbol,
                                  final List<String[]> params){

        final List<String[]> rightRules = new ArrayList<>();

        for(final String[] param : params){
            final boolean isRigthRule = isRightRule(currentState, newSimbol, param);

            if(isRigthRule)
                rightRules.add(param);
        }

        if(rightRules.size() == 0) {
            END_FLAG = true;
            ABORTED = true;
            return 0;
        }

        String[] rightRule = rightRules.get(0);

        for (int i=1; i<rightRules.size(); i++){
            final boolean shouldSwap = compareRules(rightRule, rightRules.get(i));

            if (shouldSwap)
                rightRule = rightRules.get(i);
        }

        return getNewPos(currentState, newSimbol, rightRule);
    }

    private static byte getNewPos(final StringBuilder currentState, final StringBuilder newSimbol, final String[] rightRule) {
        setString(currentState, rightRule[4]);

        if(!rightRule[2].equals("*"))
            setString(newSimbol, rightRule[2]);

        if(rightRule[4].contains("halt")){
            END_FLAG = true;
        }

        switch (rightRule[3]){
            case "l":
                return -1;
            case "r":
                return 1;
            case "*" :
                return 0;
            default:
                throw new RuntimeException("Valor invalido!");
        }
    }

    private static boolean compareRules(final String[] rightRule, final String[] strings){
        final int[] points = new int[2];

        points[0] = getPoints(rightRule);
        points[1] = getPoints(strings);

        return points[1] > points[0];
    }

    private static int getPoints(final String[] array){
        int response = 0;

        if(!array[0].equals("*"))
            response++;

        if(!array[1].equals("*"))
            response++;

        return response;
    }

    private static boolean isRightRule(final StringBuilder currentState,
                                       final StringBuilder newSimbol,
                                       final String[] param) {

        if(currentState.toString().equals(param[0]) || param[0].equals("*")){
            return newSimbol.toString().equals(param[1]) || param[1].equals("*");
        }

        return false;
    }

    private static void setString(final StringBuilder sb, String str){
        if(str.equals(" "))
            str = "_";

        sb.delete(0, sb.length());
        sb.append(str);
    }

    private static List<String[]> getParams(final String path) {
        final List<String[]> params = new ArrayList<>();

        try (final Scanner fileScan = new Scanner(new File(path))) {
            while (fileScan.hasNextLine()) {
                String lineRead = fileScan.nextLine();

                final int posComment = lineRead.indexOf(';');

                if(posComment >= 0)
                    lineRead = lineRead.substring(0, posComment).trim();

                if(lineRead.isBlank())
                    continue;

                final String[] rules = lineRead.split(" ");

                params.add(rules);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException("Could not open file with rules!", e);
        }
        
        return params;
    }
}
