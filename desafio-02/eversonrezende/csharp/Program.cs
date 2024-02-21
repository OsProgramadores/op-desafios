//Um numero primo e um numero divisivel apenas por 1 e por ele mesmo

for (int i = 1; i <= 10000; i++)
{
  //Numero 1 nao e primo
  if (i == 1)
  {
    continue;
  }

  // Usando a ferramenta "Crivo de Eratostenes"
  // Consiste em 4 passos

  //Passo 1 - Numeros divisiveis por 2: Numeros pares sao todos divisiveis por 2
  //ou seja, terao como divisores o proprio numero, 1 e 2
  //logo nao sao primos (exceto o 2)
  if (i != 2 && i % 2 == 0)
  {
    continue;
  }

  //Passo 2 - Numeros divisiveis por 3
  if (i != 3 && i % 3 == 0)
  {
    continue;
  }

  //Passo 3 - Numeros divisiveis por 5, ou seja, que terminam em 0 e 5.
  if (i != 5 && i % 5 == 0)
  {
    continue;
  }

  //Passo 4 - Excluir multiplos de 7
  if (i != 7 && i % 7 == 0)
  {
    continue;
  }

  Console.WriteLine(i);
}
