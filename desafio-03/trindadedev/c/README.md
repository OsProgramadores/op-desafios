# Palíndromos
Número que invertidos, são iguais.

# Como funciona?
Esse programa basicamente inverte o inteiro e verifica se ele é igual ao original.
Se for igual, então ele é palíndromo, do contrário, não.

## Começo do programa
a função "main" do programa, verifica se todos os argumentos foram passados.
se sim, então verifica se o conteúdo da String(char*) são digitos, ou seja inteiros.
se forem, então converte a String(char*) do parâmetro, para inteiro.
caso contrário, o usuário é notificado de falha.

## Como o inteiro é invertido?
Basicamente usei o código de [StackOverflow](https://pt.stackoverflow.com/questions/37031/inverter-um-n%C3%BAmero-de-3-d%C3%ADgitos-em-c)

# Como Executar?
Para compilar você pode usar algum compilador para C, como GCC (GNU Compiler Collection) do Projeto GNU, ou então CLang do Projeto LLVM.
No código abaixo mostro como você pode compilar usando GCC.

```bash
gcc main.c -o palindromes
chmod +x palindromes
./palindromes 1 20
```

## Programa escrito por Aquiles Trindade [trindadedev](https://github.com/trindadedev13)