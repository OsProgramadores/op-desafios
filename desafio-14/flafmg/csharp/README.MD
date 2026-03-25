# Desafio 14: Expressões numéricas!

## Sobre o Projeto

Este programa é um avaliador de expressões numéricas. Ele le um arquivo contendo expressões matemáticas, avalia cada uma na ordem das operações matemáticas, e retorna o resultado ou mensagens de erro específicas caso a expressão seja invalida

o projeto utiliza a **[Notação Polonesa Inversa](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_polonesa_inversa)** para realizar os cálculos

## Pré-requisitos

- [.NET SDK 9.0](https://dotnet.microsoft.com/download/dotnet/9.0)

## Como usar


### 1. Clonar o repositório
```bash
   git clone -b desafio-14 https://github.com/flafmg/op-desafios.git
   cd op-desafios/desafio-14/flafmg/csharp
```

### 2. Preparar o arquivo de entrada

Crie um arquivo de texto com as expressões matemáticas que deseja avaliar tendo uma por linha.

exemplo: (`expressoes.txt`):

```
1 + 3
2 - 3 * 2
2 ^ 3 / 4
0 * 5 * (4 + 1)
5 + 5 / 0
5 + + 1
5 + ( 465 + 1
```

### 3. Executar o programa
```bash
dotnet run "<caminho_do_arquivo>"
```

#### Exemplo de execução
Entrada:
```bash
dotnet run "expressoes.txt"
```
saída:
```
4
-4
2
0
ERR DIVBYZERO
ERR SYNTAX
ERR SYNTAX
```