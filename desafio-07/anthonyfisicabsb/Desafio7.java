import java.util.*;
import java.io.*;

public class Desafio7
{
    public static void main(String[] args)
    {
        if(args.length != 1) {
            System.out.println("Digite java -jar Desafio07.jar <nome-arquivo>");
            return;
        }

        BufferedReader in;

        try {
            in = new BufferedReader(new FileReader(args[0]));
            String primeiraLinha = in.readLine();
            String ultimaLinha = "";
            String aux = "";

            while((aux = in.readLine()) != null){
                ultimaLinha = new String(aux);
            }

            System.out.println(ultimaLinha);

            in.close();

            if(primeiraLinha == null)
                System.exit(0);

            while(!ultimaLinha.equals(primeiraLinha)) {
                in = new BufferedReader(new FileReader(args[0]));

                String aux2 = "";

                while(!(aux = in.readLine()).equals(ultimaLinha)){
                    aux2 = new String(aux);
                }

                System.out.println(aux2);

                ultimaLinha = new String(aux2);
                in.close();
            }
        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}
