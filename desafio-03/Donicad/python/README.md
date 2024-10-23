# Script para exibir todos os números polindromos

## Requisitos

- Ter Python instalado em seu computador

    Faça o download da versão mais atual do python para seu sistema operacional no site oficial da linguagem [python.org](https://www.python.org/downloads/).

## Funcionamento

Ao executar o arquivo n_polindromo.py em uma IDE de sua preferência um numero inicial e final será requisitado no terminal.
Após preencher os dois números, o script irá percorrer do número inical ao final exibindo no terminal todos os números que são polindromos.


## Explicação do Código

```python
    try:
        numero_incial = int(input("Digite um numero inicial: "))
        numero_final = int(input("Digite um numero final: "))
        if numero_incial < 0 or numero_final < 0:
            raise ValueError("Apenas números positivos")
    except ValueError as erro:
        print(f"Erro: {erro}")

```
- essa primeira parte do script é responsavél por inciar os inputs do número inicial e final, e em seguida é feita uma verificação para ver se algum número digitado nos inputs é negativo. Se for, então o programa alerta que apenas números positivos podem ser colocados e encerra o script.

---

```python
    numeros_palindromos = []

    for numero in range(numero_incial, numero_final + 1):
        if str(numero) == str(numero)[::-1]:
            numeros_palindromos.append(numero)
```

- Criei uma variável com uma lista vazia para armazenar todos os numeros polindromos.

- Com um laço for inciando uma sequência do número inicial para o final. 
O (+ 1) junto com o numero final serve para que o numero final digitado pelo usuario seja adicionado na leitura do range().

- Depois do laço uma verificação é feita para saber se o número armazenado na variável "numero" é igual a ele mesmo, porém é utilizado o parametro"[::-1]" pois com isso o script vai comparar com a versão invertida do número. Para ajudar essa verificação os dois números armazenados são transformados em string(str) ou seja, em textos, pois dessa forma podemos até mesmo analisar números grandes com suas versões invertidas.

```python
    if numeros_palindromos:
        print(numeros_palindromos)
```

- Essa verificação feita antes do print é para saber se a lista contém algum número ou não, se caso a lista estiver com números armazenados, então eles devem ser impressos no terminal.

- Essa verificação é util para os casos de se colocar um número negativo nos inputs, dessa forma a lista não será printada, apenas a mensagem de erro.
