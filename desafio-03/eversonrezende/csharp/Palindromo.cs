namespace csharp;

public static class Palindromo
{
  public static List<int> GetPalindromos(int inicial, int final)
  {
    if (inicial < 0 || final < 0)
    {
      throw new Exception("Os números devem ser maiores que zero.");
    }

    if (inicial > final)
    {
      throw new Exception("O número inicial deve ser menor que o número final.");
    }

    bool resultado;
    var listaPalindromos = new List<int>();
    int contador = 0;

    for (int i = inicial; i <= final; i++)
    {
      resultado = IsPalindromo(i);

      if (resultado)
      {
        for (int j = contador; j <= final; j++)
        {
          listaPalindromos.Add(i);
          break;
        }
      }
    }
    return listaPalindromos;
  }

  private static bool IsPalindromo(int numero)
  {
    var charNumero = numero.ToString().ToCharArray();
    char[] chars = charNumero;
    char[] inverse = new char[charNumero.Length];
    bool isPalindromo = true;

    for (int i = 0; i < charNumero.Length; i++)
    {
      for (int j = charNumero.Length - 1 - i; j >= 0; j--)
      {
        inverse[i] = chars[j];
        break;
      }
    }

    for (int i = 0; i < charNumero.Length; i++)
    {
      for (int j = i; j < charNumero.Length; j++)
      {
        if (chars[i] != inverse[j])
        {
          isPalindromo = false;
          break;
        }
        break;
      }

      if (!isPalindromo)
      {
        break;
      }
    }
    return isPalindromo;
  }
}