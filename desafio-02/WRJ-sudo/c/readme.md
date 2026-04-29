# Algoritmo de Números Primos

## Descrição
Este algoritmo é capaz de encontrar todos os números primos até 10.000.

## Requisitos
-Possuir o GCC ou outro compilador para linguagem C instalado no sistema operacional.
Para a execução do código é preciso acessar o terminal e digitar o comando `gcc nomedoprograma.c -o nomeparaobject'`

## Método Utilizado
O programa utiliza o algoritmo **Crivo de Eratóstenes**, que permite obter os números primos de forma eficiente.

## Lógica do Algoritmo
- É utilizado um vetor onde:
  - O **índice representa o número analisado**.
  - O **valor armazenado indica se o número é primo ou não**:
    - `1` → primo  
    - `0` → não primo  

- Inicialmente:
  - Todos os números são considerados primos.
  - Exceto:
    - `0` e `1`, que não são primos.

- Em seguida:
  - O algoritmo percorre os números e elimina os múltiplos de cada número primo encontrado.
