//Algoritmo - Crivo de Erastotenes

//Valor Limite
var valorLimite = 10000;

//Maior numero a ser verificado, ele corresponde a raiz quadrada do valor limite, arredondando pra baixo.
var maiorNumeroVerificado = Math.Floor(Math.Sqrt(valorLimite));

//Criar uma lista de todos os numeros inteiros de 2 ate o valor limite.
List<int> listaPrimos = new();

for (int i = 2; i <= valorLimite; i++)
{
  listaPrimos.Add(i);
}

//Comecando em 2 (i), percorra a lista e remova todos os multiplos de i ate o valor limite. 
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

//Apos a verificacao acima, sobram apenas os numeros primos
foreach (var numero in listaPrimos)
{
  Console.WriteLine(numero);
}