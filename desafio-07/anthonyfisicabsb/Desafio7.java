import java.io.RandomAccessFile;
import java.io.IOException;

public class Desafio7
{
    public static void main(String[] args) throws IOException
    {
        if(args.length != 1) {
            System.out.println("Digite java -jar Desafio07.jar <nome-arquivo>");
            return;
        }

        RandomAccessFile ptr = null;
        long posPtr = 0;
        long posAtual = 0;
        String impressao = "";
        byte[] caracteres = null;
        char test = 'a';

        try {
            ptr = new RandomAccessFile(args[0], "r");

            posPtr = ptr.length() -1;
            posAtual = posPtr - 1;

            do{
                posAtual--;

                    ptr.seek(posAtual);
                    if((test = (char)ptr.read()) == '\n'){
                        ptr.seek(posAtual + 1);

                        caracteres = new byte[(int)posPtr - (int)posAtual];
                        ptr.readFully(caracteres);
                        impressao = new String(caracteres, "UTF-8");
                        posPtr = posAtual;

                        System.out.print(impressao);
                    }
            }while(posAtual > 0);

        }catch(Exception e) {
        }finally {
            ptr.seek(0);

            caracteres = new byte[(int)posPtr + 1];
            ptr.readFully(caracteres);

            impressao = new String(caracteres, "UTF-8");

            System.out.print(impressao);
        }
    }
}
