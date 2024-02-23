# Desafio 2: Números primos

![C#](https://img.shields.io/badge/C%23-512BD4?style=flat&logo=csharp&logoColor=white) ![.NET 8.0](https://img.shields.io/badge/.NET-v8.0-blue?logo=dotnet) ![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Proposta

Este programa é uma solução para o [Desafio #02](https://osprogramadores.com/desafios/d02/) proposto pelo grupo [OsProgramadores](https://osprogramadores.com/). Desenvolvido em C#, o código tem como propósito listar todos os números primos dentro do intervalo de 1 a 10000.

Para participar também dos desafios, visite a página em [osprogramadores.com/desafios](https://osprogramadores.com/desafios/) e confira todos os desafios.

## Como funciona o código?

A função `bool EhPrimo(int num)` recebe um número inteiro como parâmetro e verifica se é primo ou não. Se o número for primo, a função retorna `true`; caso contrário, retorna `false`, indicando que não é primo.

O loop `for (int i = 0; i < 10000; i++)` varre cada número de 0 a 9999, passando-os à verificação da função `EhPrimo` para listar os números primos dentro deste intervalo. Os números primos são então impressos usando o comando `Console.WriteLine`, que exibe o resultado no console.

## Ferramentas Utilizadas

**Ambiente de Desenvolvimento Integrado (IDE):**

- **Visual Studio Code**

O Visual Studio Code foi escolhido como a IDE para o desenvolvimento deste desafio. Você pode baixar o VS Code em [Baixar Visual Studio Code](https://code.visualstudio.com/download).

**Kit de Desenvolvimento:**

- **.NET 8.0**

Utilizei o .NET 8.0 como Kit de Desenvolvimento para garantir compatibilidade e aproveitar as funcionalidades mais recentes da linguagem. O .NET está disponível para download em: [Baixar .NET 8.0](https://dotnet.microsoft.com/pt-br/download/dotnet/8.0).

## Como executar o código?

Para executar o código do desafio, é necessário ter as ferramentas mencionadas acima instaladas. Em seguida, basta abrir o terminal do VS Code e inserir o seguinte comando:

```cmd
dotnet run
```