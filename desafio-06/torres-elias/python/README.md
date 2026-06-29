# Desafio 06 - Anagramas

## Descrição

Um programa que recebe uma expressão e imprime todos os anagramas possíveis dentro do conjunto de palavras presente em "words.txt".

## Solução

O programa recebe a expressão como argumento, converte tudo para maiúsculo e ignora os espaços. Em seguida, lê o arquivo `words.txt` e filtra apenas as palavras que cabem nas letras disponíveis. Por fim, usa backtracking para encontrar todas as combinações possíveis.

## Como executar

```bash
python anagramas.py <expressao>
```

Testado com Python 3.10.
