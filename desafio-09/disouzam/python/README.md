# Introdução

Esse programa lê linhas de um arquivo texto fornecido como parâmetro, contendo uma lista de três numeros por linha: `base_entrada`, `base_saida` e `numero_entrada` e imprime o número após conversão para a base de saída.

O formato exato da entrada é:

`base_entrada` `base_saida` `numero_entrada`

Um exemplo apresentado na página do desafio é:

```text
10 16 1500
36 10 GOODBYE
36 16 HELLOWORLD
10 2 32452867
2 10 1234
```

E o resultado para esse exemplo é:

```text
5DC
36320638406
647B8839EB1B1
1111011110011000100000011
???
```

# Verificação do código com Pylint

O comando a seguir altera o diretório para a pasta do desafio:

```shell
cd desafio-09/disouzam/python
```

Executando dentro da pasta do desafio (desafio-09/disouzam/python), o comando para verificar o código através do Pylint é:

```python
pylint --rcfile=../../../ci/pylint3.rc big_base.py
```

# Como executar o script

Esse código foi testado com a versão 3.11.2 do Python e pode apresentar alguma instabilidade com o Python 3.11.8 (não foi checado contra essa versão).

Executando dentro da pasta do desafio (desafio-09/disouzam/python), o comando é:

```python
python -m big_base "exemplo_entrada.txt"
```

# Testes para desenvolvimento

Como base para desenvolvimento e checagem dos resultados, o exemplo disponível na página do desafio foi reproduzido no arquivo `exemplo_entrada.txt`

```python
python -m big_base "exemplo_entrada.txt"
```

# Referência:

- [Floor division in Python](https://www.geeksforgeeks.org/floor-division-in-python/)