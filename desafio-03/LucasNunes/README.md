# 🔢 Números Palindrômicos

## 📖 Visão geral

Este projeto foi desenvolvido em Python com o objetivo de encontrar todos os números palindrômicos dentro de um intervalo definido.

Um número palindrômico é aquele que mantém o mesmo valor quando lido de trás para frente.

### Exemplos:

```bash
121 → 121
202 → 202
303 → 303
```

Já números como:

```bash
123 → 321
456 → 654
```

não são palíndromos.

---

## 🎯 Objetivo

Treinar lógica de programação, manipulação de strings e resolução de problemas utilizando Python.

---

## 🛠️ Tecnologias utilizadas

- Python

---

## ⚙️ Como funciona

O programa:

1. Percorre todos os números do intervalo utilizando `for`.
2. Converte cada número para `string`.
3. Inverte o número utilizando slicing.
4. Compara o número original com sua versão invertida.
5. Exibe apenas os números palindrômicos.

---

## 🧠 Lógica utilizada

A verificação principal acontece da seguinte forma:

```python
if numero == numero[::-1]:
```

### Explicação:

- `numero[::-1]` percorre a string ao contrário.
- Se o valor original for igual ao invertido, o número é palíndromo.

---

## 💻 Código principal

```python
for numero in range(100, 10001):

    numero = str(numero)

    if numero == numero[::-1]:

        print(numero)
```

---

## 📌 Conceitos praticados

- Estrutura de repetição `for`
- Estrutura condicional `if`
- Conversão de tipos com `str()`
- Manipulação de strings
- Slicing
- Comparação de valores
- Lógica de programação

---

## ▶️ Exemplo de saída

```bash
101
111
121
131
141
151
161
171
181
191
202
212
222
```

---

## 🚀 Aprendizados

Durante este desafio pratiquei:

- Como quebrar um problema em partes menores.
- Como transformar números em strings.
- Como utilizar slicing para inverter valores.
- Diferença entre `int` e `string`.
- Como identificar padrões utilizando lógica de programação.