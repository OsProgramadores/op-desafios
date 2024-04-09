import java.text.MessageFormat;

public class PrimeNumbers
{

	public static void main(String[] args)
	{
		// For para iterar entre 2 e 10000
		for (int i = 1; i <= 10000; i++)
		{
			if(isPrime(i))
			{
				System.out.println(i);
			}
		}
	}

	//Função para verificar se o numero é primo
	public static boolean isPrime (int num)
	{
		if(num < 2)
		{
			return false;
		}

		for (int i = 2; i <= num / 2; i++)
		{
			if (num % i == 0)
			{
				return false;
			}

		}
		return true;
	}
}
