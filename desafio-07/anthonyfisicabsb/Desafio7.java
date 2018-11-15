import java.io.RandomAccessFile;
import java.io.IOException;
import java.util.ArrayList;

/*
    Programa que resolve o desafio do site osprogramadores.com.
    O desafio consiste em implementar a função nativa tac do linux,
    que lê os arquivos e os imprime em ordem reversa.
*/

public class Desafio7
{
    public static void main(String[] args) throws IOException
    {
        if(args.length != 1) {
            System.out.println("Digite java Desafio07 <nome-arquivo>");
            return;
        }

        final int sizeArray = 1000000; // tamanho em bytes do array

        long posPtr = 0;
        long posAtual = 0;
        byte[] charChunk = null;
        final ArrayList<Byte> listaImpressao = new ArrayList<>();

        try {
            final RandomAccessFile ptr = new RandomAccessFile(args[0], "r");

            posPtr = ptr.length();

            do{
                posAtual = (posPtr - sizeArray) < 0 ? 0: (posPtr - sizeArray);
                ptr.seek(posAtual);

                charChunk = new byte[(int)posPtr - (int)posAtual];
                ptr.readFully(charChunk);

                readArray(charChunk, listaImpressao);

                posPtr = posAtual;

            }while(posPtr > 0);

            printString(listaImpressao);

        }catch(Exception e) {
            throw new RuntimeException("Ocorreu algum erro", e);
        }
    }

    public static void readArray(byte charChunk[], ArrayList<Byte> impressao) throws Exception
    {
        for(int i = charChunk.length - 1; i >= 0; i--){
            if((char)charChunk[i] == '\n'){
                printString(impressao);
                impressao.clear();
            }

            impressao.add(0, charChunk[i]);
        }
    }

    public static void printString(ArrayList<Byte> lista) throws Exception 
    {
        final byte bytes[] = new byte[lista.size()];

        for(int i=0; i < lista.size(); i++){
            bytes[i] = lista.get(i);
        }

        final String impressao = new String(bytes, "UTF-8");

        System.out.print(impressao);
    }
}
