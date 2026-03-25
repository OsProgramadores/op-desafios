using System;

namespace palindromos;

public class Palindromo
{
    public Palindromo() { }

    public bool EhPalindromo(ulong numero){
        // Converte o número para uma string.
        string numeroStr = numero.ToString();

        // Inverte a string.
        char[] charArray = numeroStr.ToCharArray();
        Array.Reverse(charArray);
        string numeroInvertidoStr = new string(charArray);

        // Compara a string original com a string invertida.
        return numeroStr.Equals(numeroInvertidoStr);
    }

    public List<ulong> PalindromosEntre(string inicio, string fim)
    {
        ValidarParametros(inicio);
        ValidarParametros(fim);

        List<ulong> resultado = new List<ulong>();

        for (ulong i = UInt64.Parse(inicio); i <= UInt64.Parse(fim); i++)
        {
            if (EhPalindromo(i))
            {
                resultado.Add(i);
            }
        }

        return resultado;
    }

    private static void ValidarParametros(string numero)
    {
        try
        {
            var conversao = UInt64.Parse(numero);
        } catch (OverflowException)
        {
            throw new OverflowException("Valor maior ou menor que o permitido");
        } catch (ArgumentNullException)
        {
            throw new ArgumentNullException("Valor não pode ser nulo");
        } catch (FormatException)
        {
            throw new FormatException("Valor inválido");
        }
    }
}
