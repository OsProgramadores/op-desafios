# Introdução

Processa uma palavra ou frase e retorna todas as combinações possíveis de anagramas com palavras presentes no arquivo desafio-06/disouzam/python/words.txt (cópia local do arquivo disponível em https://osprogramadores.com/desafios/d06/words.txt)


# Verificação do código com Pylint

O comando a seguir altera o diretório para a pasta do desafio:

```shell
cd desafio-08/disouzam/python
```

Executando dentro da pasta do desafio (desafio-08/disouzam/python), o comando para verificar o código através do Pylint é:

```python
pylint --rcfile=../../../ci/pylint3.rc anagrama.py
```

# Como executar o script

Esse código foi testado com a versão 3.11.2 do Python e pode apresentar alguma instabilidade com o Python 3.11.8 (não foi checado contra essa versão).

Executando dentro da pasta do desafio (desafio-08/disouzam/python), o comando é (com uma palavra de exemplo):

```python
python -m anagrama "vermelho"
```

Exemplo com uma frase:

```python
python -m anagrama "oi gente"
```

Ambos os exemplos foram extraídos do texto original do desafio no site [OsProgramadores](https://osprogramadores.com/desafios/d06/)

Exemplos com caracteres inválidos:

```python
python -m anagrama "Hello world!"
```

```python
python -m anagrama "Hello world! Hoje é dia 24 de março de 2024."
```

# Referências

- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Advanced Python with Joe Marini](https://www.linkedin.com/learning/advanced-python/function-documentation-strings)