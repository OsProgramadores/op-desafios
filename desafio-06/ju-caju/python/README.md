# Desafio 06

## Informações sobre a implementação

Esta solução recebe uma expressão pela linha de comando, remove os espaços, converte o texto para maiúsculas e valida se existem apenas letras.

Depois disso, o programa conta as letras disponíveis, carrega palavras de um arquivo `words.txt` e usa busca recursiva com retrocesso para montar combinações que usem exatamente as letras da expressão original.

Os anagramas encontrados são impressos em ordem.

## Como rodar o exercício

Entre na pasta da solução:

```bash
cd desafio-06/ju-caju/python
```

Este programa precisa de um arquivo `words.txt` na mesma pasta do `resposta.py`.

Depois execute:

```bash
python3 resposta.py "sua expressao aqui"
```

Exemplo:

```bash
python3 resposta.py "oi gente"
```

## Como instalar o Python

Se o Python 3 já estiver instalado, você pode confirmar com:

```bash
python3 --version
```

Se não estiver instalado, no Ubuntu ou Debian rode:

```bash
sudo apt update
sudo apt install python3
```
