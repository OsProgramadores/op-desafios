# Introdução

> Uma Máquina de Turing é um modelo computacional matemático que define uma máquina abstrata.
> Essa máquina manipula símbolos numa fita de papel de acordo com uma tabela de regras simples.
> Apesar da simplicidade do modelo, é possível construir uma Máquina de Turing capaz de simular
> qualquer algoritmo computacional. Fonte: https://osprogramadores.com/desafios/d10/

Esse programa implementa uma versão da máquina de Turing conforme descrito no link citado acima
na linguagem Python.

# Verificação do código com Pylint

O comando a seguir altera o diretório para a pasta do desafio:

```shell
cd desafio-10/disouzam/python
```

Executando dentro da pasta do desafio (desafio-10/disouzam/python), o comando para verificar o
código através do Pylint é:

```python
pylint --rcfile=../../../ci/pylint3.rc turing_machine.py
```

# Como executar o script

Esse código foi testado com a versão 3.11.2 do Python e pode apresentar alguma instabilidade com
o Python 3.11.8 (não foi checado contra essa versão).

Executando dentro da pasta do desafio (desafio-10/disouzam/python), o comando é:

```python
python -m turing_machine datafile
```

# Referências

- [Turing Machines Explained - Computerphile](https://www.youtube.com/watch?v=dNRDvLACg5Q)
- [Turing Machine Primer - Computerphile](https://www.youtube.com/watch?v=DILF8usqp7M)