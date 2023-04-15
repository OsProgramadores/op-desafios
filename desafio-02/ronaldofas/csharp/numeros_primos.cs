
public class numeros_primos
{
    public static void Main()
    {
        // Desafio - Imprimir números primos entre 1 e 10.000
        List<int> numeros_primos = new List<int>();
        int numeroInicial = 1;
        int numeroFinal = 10000;

        for (int i = numeroInicial; i <= numeroFinal; i++)
        {
            if (NumeroEhPrimo(i))
            {
                numeros_primos.Add(i);
            }
        }

        ImprimeCabecalho(23, $"Números primos entre {numeroInicial} e {numeroFinal} ");
        ImprimePrimos(numeros_primos);
        ImprimeCabecalho(31, "Fim da execução!");
    }

    public static bool NumeroEhPrimo(int numero){
        int quantidadeDivisores = 0;

        for (int i = 1; i <= numero; i++)
        {
            if (numero % i == 0)
            {
                quantidadeDivisores ++;
            }

            if (quantidadeDivisores > 2 || numero == 1)
            {
                return false;
            }
        }

        return true;
    }

    public static void ImprimeCabecalho(int qtdCaracter, string texto)
    {
        string desenhoComCarater = "";

        for (int i = 1; i <= qtdCaracter; i++){
            desenhoComCarater = desenhoComCarater + "=";
        }

        Console.WriteLine(desenhoComCarater + " " + texto + " " + desenhoComCarater);
    }

    public static void ImprimePrimos(List<int> numeros)
    {
        List<int> linha = new List<int>();

        for (int i = 0; i < numeros.Count; i++){
            linha.Add(numeros[i]);

            if(linha.Count % 10 == 0){
                for(int a = 0; a < linha.Count; a++){
                    Console.Write(linha[a].ToString() + ", ");
                }
                Console.Write("\n");
                linha.RemoveAll(n => n <= numeros.Max());
            }
        }

        if (linha.Count > 0){
            for(int a = 0; a < linha.Count; a++){
                if(a == linha.Count - 1)
                    Console.Write(linha[a].ToString());
                else
                    Console.Write(linha[a].ToString() + ", ");
            }
            Console.Write("\n");
        }
    }
}
