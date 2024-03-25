# Introdução

Processa uma palavra ou frase e retorna todas as combinações possíveis de anagramas com palavras presentes no arquivo desafio-06/disouzam/python/words.txt (cópia local do arquivo disponível em https://osprogramadores.com/desafios/d06/words.txt)


# Verificação do código com Pylint

Executando dentro da pasta do desafio (desafio-06/disouzam/python), o comando é:

```python
pylint --rcfile=../../../ci/pylint3.rc anagrama.py
```

# Como executar o script

Executando dentro da pasta do desafio (desafio-06/disouzam/python), o comando é (com uma palavra de exemplo):

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