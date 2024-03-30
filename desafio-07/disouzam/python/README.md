# Introdução

Implementação do comando _tac_ que lê um arquivo e exibe as linhas em ordem inversa - da última para a primeira


# Verificação do código com Pylint

O comando a seguir altera o diretório para a pasta do desafio:

```shell
cd desafio-07/disouzam/python
```

Executando dentro da pasta do desafio (desafio-07/disouzam/python), o comando para verificar o código através do Pylint é:

```python
pylint --rcfile=../../../ci/pylint3.rc tac.py
```

# Como executar o script

Esse código foi testado com a versão 3.12.1 do Python e pode apresentar alguma instabilidade com o Python 3.11 (não foi checado contra essa versão).

Executando dentro da pasta do desafio (desafio-07/disouzam/python), o comando é (com uma palavra de exemplo):

```python
python -m tac 1GB.txt
```

# Referências