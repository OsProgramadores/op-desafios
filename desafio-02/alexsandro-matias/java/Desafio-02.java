package programadores;

public class Desafio02
{
	public static void main(String[] args)
	{
		for (int j = 2; j < 1000; j++)
		{
			int contador = 0;
			for (int i = 1; i <= j; i++)
			{
				if ((j % i) == 0)
				{
					contador++;
				}
			}
			if (contador == 2)
			{
				System.out.println(j);
				j++;
			}
		}
	}
}
