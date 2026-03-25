using System;

class Program{

    public static void Main(string[] args){
        ListarPrimos();
    }

    static void ListarPrimos()
    {
        Console.WriteLine("Imprime números primos de 1 a 10000");
        for(int i=1;i<=10000;i++)
        {
            if(EhPrimo(i))
            {
                Console.WriteLine(i);
            }
        }
    }

    static bool EhPrimo(int n)
    {
        if(n <= 1) return false;
        int count = 0;
        for(int i = 1; i <= n; i++)
        {
            if(n % i == 0) count++;

            if (count > 2) return false;
        }   
        return true;
    }
}