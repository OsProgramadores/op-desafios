# Desafio 04 - Palíndromos

O exercício proposto pelo desafio é a geração de números palíndromos dentro do intervalo fornecido

A solução implementada em Java segue a seguinte estratégia:
- Identificar o número de dígitos dos valores mínimos e máximos
- Fazer uma repetição indo do número de dígitos do valor mínimo até o número de dígitos do valor máximo
- A cada iteração, gera todos os palíndromos com _N_ dígitos e filtra (se necessário)

## Requisitos

- Java 8 ou superior

## Compilação

```
javac PalindromeNumbers.java
```

## Execução

- Com intervalo padrão (0 a 1000)
```
java PalindromeNumbers
```

- Com intervalo definido (15 a 70)
```
java PalindromeNumbers 15 70
```
