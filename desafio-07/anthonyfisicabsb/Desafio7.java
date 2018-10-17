import java.io.BufferedReader;
import java.io.FileReader;

public class Desafio7
{
    public static void main(String[] args)
    {
        if(args.length != 1) {
            System.out.println("Digite java Desafio07 <nome-arquivo>");
            return;
        }

        BufferedReader in;

        try {
            in = new BufferedReader(new FileReader(args[0]));

            String ultimaLinha = "";
            int numUltimaLinha = 0;
            String aux = "";

            while((aux = in.readLine()) != null){
                ultimaLinha = new String(aux);
                numUltimaLinha++;
            }

            System.out.println(ultimaLinha);

            in.close();

            while(numUltimaLinha != 1) {
                in = new BufferedReader(new FileReader(args[0]));
                int count = 1;

                while(count < numUltimaLinha){
                    count++;
                    ultimaLinha = in.readLine();
                }

                System.out.println(ultimaLinha);
                numUltimaLinha--;
                in.close();
            }
        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}
