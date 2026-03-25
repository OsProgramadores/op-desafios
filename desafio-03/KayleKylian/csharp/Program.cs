for (int num = 1; num < 64; num++)
{
    string numString = num.ToString();
    char[] numArray = numString.ToCharArray();

    Array.Reverse(numArray);

    string result = String.Join("", numArray);
    if (result == numString) Console.WriteLine($"Palíndromo: {num}");
}