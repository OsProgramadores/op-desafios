# Script para exibir todos os números primos de 1 a 1000

## Requisitos

- Ter Python instalado em seu computador

    Faça o download da versão mais atual do python para seu sistema operacional no site oficial da linguagem [python.org](https://www.python.org/downloads/).


## Funcionamento

Ao executar o arquivo n_primos.py em uma IDE de sua preferência a função "primos" irá iniciar e impressão no terminal exibindo apenas os números primos

## Estrutura da função primos()

a função recebe duas listas, uma vazia para armazenar os números primos e outra para os números de 1 a 1000.

```python
    def primos():
    list_primos = [] 
                  #range(start, stop)
    numeros = list(range(1, 1001))
```
- start : se inicia com o número 1
- stop : finaliza no número 1001 para que a sequência siga até o 1000 pois o ultimo digito não é incluído.

___

```Python
    for n in numeros:
```
Um laço é criado percorrendo todos os números na lista numeros de 1 a 1000. O número atual no laço é representado por n.

___

```Python
    if n > 1
```
Uma condição é feita por o 1 não é considerado número primo, então o cálculo só deve ser feito com números maiores.

___

```Python
    for i in range(2, n):
```
laço for começa no número 2 e vai até n-1. Ele verifica se o número n é divisível por algum número dentro dessa sequência.

___

```Python
    if (n % i) == 0:
```
Nesse if é verificado se n é divisível por i. O operador % retorna o resto da divisão. Se o resto for zero, isso significa que n é divisível por i, e por conta disso o n não é um número primo.

___

```Python
    break
```
Se n for divisível por qualquer número i no intervalo de 2 até n-1, o laço interno é interrompido com o comando break. Isso evita verificar mais divisores.

___

```Python
    else:
        list_primos.append(n)
```

A estrutura else está associada ao laço for. Esse bloco será executado se o laço for não for interrompido pelo break, ou seja, se o número n não tiver sido divisível por nenhum número entre 2 e n-1. Se isso acontecer, n é um número primo e, portanto, é adicionado à lista list_primos.

Após o término dos laços, a função retorna a lista list_primos, que agora contém todos os números primos de 1 a 1000.

___

```Python
    for primo in primos():
        print(primo)
```
E para executar a função primos é feito um laço para percorrer todos os numeros armazenados na lista e exibir no terminal uma baixo do outro.