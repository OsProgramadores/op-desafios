using csharp;

Console.WriteLine("Número inicial: ");
var numeroIni = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Número final: ");
var numeroFim = Convert.ToInt32(Console.ReadLine());

var listaPalyndromo = Palindromo.GetPalindromos(numeroIni, numeroFim);

foreach (var item in listaPalyndromo)
{
  Console.WriteLine(item);
}
