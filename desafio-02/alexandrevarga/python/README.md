

# Desafio 02 - Números Primos

Este projeto faz parte do Desafio 02 da comunidade Os Programadores.

O objetivo é encontrar e imprimir todos os números primos em um intervalo específico utilizando Python.


## 📋 Descrição

O programa implementa uma função que identifica todos os números primos dentro de um intervalo (por padrão, de 1 a 10.000) e imprime cada primo em uma linha. O código segue as boas práticas do Python (PEP 8) e está devidamente documentado.


## 📁 Estrutura

O arquivo principal está localizado em:

desafio-02/
└── alexandrevarga/
    └── python/
        └── primos.py


## 🚀 Como Executar

1. **Clone este repositório:**

git clone https://github.com/OsProgramadores/op-desafios.git
cd op-desafios/desafio-02/alexandrevarga/python/

2. **Execute o script:**

python3 primos.py

3. **Saída esperada:**  

Todos os números primos entre 1 e 10.000 serão impressos, um por linha.


## 🧩 Sobre o Algoritmo

- O algoritmo percorre todos os números do intervalo.
- Para cada número, verifica se ele é primo testando divisores até sua raiz quadrada.
- Os números primos encontrados são armazenados em uma lista e impressos ao final.


## 🧹 Qualidade e Padrão de Código

### 🔎 O que é o Pylint?

Pylint é uma ferramenta que analisa o código Python em busca de erros, más práticas e problemas de estilo, verificando se ele segue o padrão PEP 8 (guia de estilo oficial do Python).

### Como instalar o Pylint

pip install pylint

### Como executar a verificação

Navegue até o diretório do arquivo

cd op-desafios/desafio-02/alexandrevarga/python/

Execute:

pylint primos.py

Ao executar o comando acima, você verá:
- Uma lista de mensagens indicando pontos para melhoria
- Uma nota geral para o código