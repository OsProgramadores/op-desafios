# Crivo de Eratóstenes: Números primos de 1 a 10000

O seguinte programa é uma implementação do algoritimo de Crivo de Eratóstenes para identificar e
listar todos os números primos de 1 a 10000.

O Crivo de Eratóstenes é um dos algoritmos mais eficientes quando se trata de listagem de números
primos menores que um valor n, apresentando uma complexidade de tempo O(nloglogn)

# Como funciona

O processo funciona eliminando os números múltiplos de um número primo encontrado.

1. É criado uma lista de 2 até n
2. Começando pelo primeiro número primo (n = 2) e eliminando seus múltiplos
3. Vai para o próximo número da lista e repete o processo
4. O algoritimo para quando p² > n

# Tecnologias utilizadas

Linguagem: Java 8+

# Execução

Para rodar o programa, basta seguir os seguintes passos

1. Esteja no diretório onde a classe se encontra
2. Rode no terminal:
```bash
$ java MeuPrograma.java
```
# Saída

Ao executar o programa você verá uma lista de números primos de 1 a 10000, um por linha
```java
2
3
5
...
9949
9967
9973
