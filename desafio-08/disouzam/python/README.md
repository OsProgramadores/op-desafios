# Introdução

Processa um arquivo texto ([frac.txt](https://osprogramadores.com/files/d08/frac.txt.gz)) contendo uma lista de frações em ASCII (uma fração por linha) e retorna uma fração simples, contendo uma parte inteira e uma parte fracionária. Maiores detalhes sobre o desafio podem ser conferidos na página [#8: FRAÇÕES SIMPLES](https://osprogramadores.com/desafios/d08/).


# Verificação do código com Pylint

O comando a seguir altera o diretório para a pasta do desafio:

```shell
cd desafio-08/disouzam/python
```

Executando dentro da pasta do desafio (desafio-08/disouzam/python), o comando para verificar o código através do Pylint é:

```python
pylint --rcfile=../../../ci/pylint3.rc fracoes.py
```

# Como executar o script

Esse código foi testado com a versão 3.11.2 do Python e pode apresentar alguma instabilidade com o Python 3.11.8 (não foi checado contra essa versão).

Executando dentro da pasta do desafio (desafio-08/disouzam/python), o comando é (com uma palavra de exemplo):

```python
python -m fracoes "frac.txt"
```

# Testes para desenvolvimento

Como base para desenvolvimento e checagem dos resultados, o exemplo disponível na página do desafio foi reproduzido no arquivo `exemplo_frac.txt`

```python
python -m fracoes "exemplo_frac.txt"
```

# Referências
