# Gerador de Anagramas

Este é um script em Python desenvolvido para encontrar todos os anagramas possíveis para uma palavra ou frase fornecida via linha de comando, utilizando um dicionário de palavras válidas.

## Como o código funciona

1.  **Validação e Limpeza:** O script recebe a expressão, remove os espaços, converte as letras para maiúsculas e interrompe a execução caso encontre caracteres inválidos (números, pontuações ou acentos).
2.  **Pré-filtro do Dicionário:** O arquivo `words.txt` é lido, mas as palavras são rigorosamente filtradas. O programa só guarda as palavras cujas letras estão presentes na expressão original e nas quantidades corretas. Isso reduz o volume de dados e acelera a busca.
3.  **Busca por Backtracking:** Com o dicionário filtrado, o script utiliza uma função recursiva de *backtracking*. Ele testa combinações de palavras, subtraindo as letras usadas do "estoque" disponível. Se uma combinação não atingir o tamanho exato da expressão original, o algoritmo retrocede e tenta a próxima rota.
4.  **Saída Ordenada:** Os anagramas válidos são processados para que as palavras dentro de cada linha apareçam em ordem alfabética, evitando repetições de combinações idênticas em ordens diferentes.

## Versão e Requisitos

* **Linguagem:** Python 3.14.3
* Não existem dependências externas. O script utiliza apenas a biblioteca nativa `sys`.
* O arquivo de dicionário `words.txt` deve estar obrigatoriamente no mesmo diretório do script.

## Como executar

Abra o terminal, navegue até a pasta do projeto e execute o comando passando a expressão desejada entre aspas:

```bash
python3 main.py "sua frase aqui"