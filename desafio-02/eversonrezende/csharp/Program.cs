//Algoritmo - Crivo de Erastótenes

//Valor Limite
var valorLimite = 50000;

//Maior número a ser verificado, ele corresponde à raiz quadrada do valor limite, arredondando pra baixo.
var maiorNumeroVerificado = Math.Floor(Math.Sqrt(valorLimite));

//Criar uma lista de todos os números inteiros de 2 até o valor limite.
List<int> listaPrimos = new();

for (int i = 2; i <= valorLimite; i++)
{
  listaPrimos.Add(i);
}

//Começando em 2 (i), percorra a lista e remova todos os múltiplos de i até o valor limite. 
for (int i = 2; i <= maiorNumeroVerificado; i++)
{
  for (int j = 2; j <= valorLimite; j++)
  {
    if (j % i == 0 && j != i && listaPrimos.Contains(j))
    {
      listaPrimos.Remove(j);
    }
  }
}

//Após a verificação acima, sobram apenas os números primos
foreach (var numero in listaPrimos)
{
  Console.WriteLine(numero);
}