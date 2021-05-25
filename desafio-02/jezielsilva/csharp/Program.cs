using System;

namespace numerosPrimos
{
    internal static class Program
    {
        public static void Main(string[] args)
        {
            int max = 10000;
            for(int i = 2; i<=max;i++){
                if(i == 2){
                    Console.WriteLine(i);
                }else{
                    if(i%2 == 0){
                        continue;
                    }else{
                        bool isPrime = true;
                        for(int j = 3; j<i/2;j++){
                            if(i%j == 0){
                                isPrime = false;
                                break;
                            }
                        }
                        if(isPrime){
                            Console.WriteLine(i);
                        }
                    }
                }
            }
        }
    }
}