# Script para exibir todos os números primos de 1 a 1000

## Requisitos

- Ter Python instalado em seu computador

    Faça o download da versão mais atual do python para seu sistema operacional no site oficial da linguagem [python.org](https://www.python.org/downloads/).


## Funcionamento

Ao executar o arquivo n_primos.py em uma IDE de sua preferência a função "listar_primos" irá iniciar e imprimir no terminal apenas os números primos.

## Estrutura da função listar_primos(n_final)

a função recebe um parâmetro chamado "n_final", no qual representa o máximo de numeros que queremos listar. 

```python
    primos = [True] * (n_final + 1)
```
- é criado uma lista com n_final + 1 (de 0 a n_final).
- é definido todas as posições como True. Dessa forma podemos marcar como False os que não são primos

___

```Python
    p = 2
```
A variável p é o número que será usado para identificar os múltiplos a serem eliminados. Iniciando com 2 pois números abaixo desse valor são inválidos para o cálculo.

___

```Python
    while p * p <= n_final:
        if primos[p] is True:
            for i in range(p * p, n_final + 1, p):
                primos[i] = False
        p += 1
```
Dentro desse laço, é feita uma verificação se o número p é considerado primo ainda. Se ele for, é marcado como "não primos" todos os mútiplos de p, começando de p * p. é feito isso pois qualquer múltiplo de p menor que p*p já foi marcado por múltiplos anteriores.

Após marcar os múltiplos de p, é incrementando p para o próximo número e o processo se repete.
___

```Python
    return [p for p in range(2, n_final + 1) if primos[p]]

```
Após o laço terminar, a lista primos ainda contém valores True para todos os números que são primos. Agora, é criada uma nova lista, que vai conter apenas os números que ainda estão marcados como primos(ou seja, marcados como True).

___


```Python
    for primo in listar_primos(1000):
        print(primo)

```
E para executar a função listar_primos passando um numero final a ela, é feito um laço para percorrer todos os numeros armazenados na lista e exibir no terminal uma baixo do outro.