# Script para exibir todos os números palindrômicos.

## Requisitos

- Ter Python instalado em seu computador

    Faça o download da versão mais atual do python para seu sistema operacional no site oficial da linguagem [python.org](https://www.python.org/downloads/).

## Funcionamento

Ao executar o arquivo n_palindromicos.py no terminal usando linha de comando um numero inicial e final será requisitado no terminal.
Após preencher os dois números, o script irá percorrer do número inical ao final exibindo no terminal todos os números que são palindrômicos.


## Explicação do Código

```python
    def verificar_entrada(mensagem):
        entrada = input(mensagem)
        if not entrada.isdigit():
            print("Erro: Apenas números podem ser inseridos.")
            exit()
        
        numero = int(entrada)
        if numero < 0:
            print("Erro: Apenas números positivos podem ser inseridos.")
            exit()
        
        return numero
```
- essa função é responsavél por inciar os inputs do número inicial e final, e em seguida é feita uma verificação para ver se algum número digitado nos inputs é negativo ou um texto. Se for, então o programa alerta que apenas números positivos podem ser colocados e encerra o script.

---

```python
    numero_incial = verificar_entrada("Digite um numero inicial: ")
    numero_final = verificar_entrada("Digite um numero final: ")
```
- Iniciamos a função armazenando os valores que serão obtidos através de um input em variavéis.

```python
    numeros_palindromicos = []

    for numero in range(numero_incial, numero_final + 1):
        if str(numero) == str(numero)[::-1]:
            numeros_palindromicos.append(numero)
```
- Criei uma variável com uma lista vazia para armazenar todos os numeros palindrômicos.

- Com um laço for inciando uma sequência do número inicial para o final. O (+ 1) junto com o numero final serve para que o numero final digitado pelo usuario seja adicionado na leitura do range().

- Depois do laço uma verificação é feita para saber se o número armazenado na variável "numero" é igual a ele mesmo, porém é utilizado o parametro"[::-1]" pois com isso o script vai comparar com a versão invertida do número. Para ajudar essa verificação os dois números armazenados são transformados em string(str) ou seja, em textos, pois dessa forma podemos até mesmo analisar números grandes com suas versões invertidas.

```python
    if numeros_palindromicos:
        print("Palindromos encontrados:")
        for polindromico in numeros_palindromicos:
            print(polindromico)
    else:
        print("Nenhum palindromo encontrado com esse intervalo.")
```

- Essa verificação feita antes do print é para saber se a lista contém algum número ou não, se caso a lista estiver com números armazenados, então eles devem ser impressos no terminal.
