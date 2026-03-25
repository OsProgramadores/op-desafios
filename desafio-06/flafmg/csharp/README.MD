# Desafio 6: Anagramas!

## Sobre o Projeto

Este programa é um gerador de anagramas que, dada uma expressão (palavra ou frase), encontra todas as combinações válidas de palavras que podem ser formadas utilizando as letras fornecidas. As combinações são verificadas com base em um dicionário de palavras válidas contido no arquivo `words.txt`.


## Pré-requisitos

- [.NET SDK 9.0](https://dotnet.microsoft.com/download/dotnet/9.0)

## Como usar

### 1. Clonar o repositório
```bash
   git clone -b desafio-06 https://github.com/flafmg/op-desafios.git
   cd op-desafios/desafio-06/flafmg/csharp
```

### 2. Preparar o arquivo `words.txt`

Certifique-se de que o arquivo `words.txt` está na mesma pasta do projeto. Este arquivo deve conter uma lista de palavras válidas, com uma palavra por linha.

Exemplo:
```
HELLO
WORLD
LOVE
YOU
CODERS
...
```

### 3. Executar o programa
```bash
dotnet run "<expressão>"
```

#### Exemplo de execução
Entrada:
```bash
dotnet run "oi gente"
```
Saída:
```
EGO I NET
EGO I TEN
GENE I TO
GENE TO I
GONE I TE
...
```
