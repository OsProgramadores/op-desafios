using palindromos;

namespace palindromosTest;

public class PalindromoTest
{
    [Fact]
    public void VerificaSeONumeroUmEhPalindromo()
    {
        // Given
        Palindromo palindromo = new Palindromo();
    
        // When
        bool resultado = palindromo.EhPalindromo(1);
    
        // Then
        Assert.True(resultado);
    }

    [Fact]
    public void VerificaSeONumeroOnzeEhPalindromo()
    {
        // Given
        Palindromo palindromo = new Palindromo();
    
        // When
        bool resultado = palindromo.EhPalindromo(11);
    
        // Then
        Assert.True(resultado);
    }

    [Fact]
    public void VerificarSeNumerosEntreZeroEUmSaoPalindromos()
    {
        //Given
        Palindromo palindromo = new Palindromo();
        
        //
        List<ulong> resultado = palindromo.PalindromosEntre("0", "9");
        List<ulong> esperado = new List<ulong>() { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    
        // Then
        Assert.Equal(esperado, resultado);
    }

    [Theory]
    [MemberData(nameof(DadosDeTesteNumerosUmDigito))]
    public void VerificarSeTodosOsNumerosDeUmDigitoSaoPalindromos(ulong numero)
    {
        // Given
        Palindromo palindromo = new Palindromo();
    
        // When
        bool resultado = palindromo.EhPalindromo(numero);
        
        // Then
        Assert.True(resultado);
    }

    [Fact]
    public void VerificarSeRecebeErroAoTentarConverterAPartirDeNegativos()
    {
        // Given
        Palindromo palindromo = new Palindromo();
        
        // When and Then
        var excecao = Assert.Throws<OverflowException>(() => palindromo.PalindromosEntre("-1", "100"));
        Assert.Equal("Valor maior ou menor que o permitido", excecao.Message);
    }
    
    [Fact]
    public void VerificarSeRecebeErroAoTentarConverterAPartirDeNumeroMaiorQueOPermitido()
    {
        // Given
        Palindromo palindromo = new Palindromo();
        
        // When and Then
        var excecao = Assert.Throws<OverflowException>(
            () => palindromo.PalindromosEntre("0", "18446744073709551616")
        );
        Assert.Equal("Valor maior ou menor que o permitido", excecao.Message);
    }
    
    public static IEnumerable<object[]> DadosDeTesteNumerosUmDigito()
    {
        yield return new object[] { 0 };
        yield return new object[] { 1 };
        yield return new object[] { 2 };
        yield return new object[] { 3 };
        yield return new object[] { 4 };
        yield return new object[] { 5 };
        yield return new object[] { 6 };
        yield return new object[] { 7 };
        yield return new object[] { 8 };
        yield return new object[] { 9 };
    }
}
