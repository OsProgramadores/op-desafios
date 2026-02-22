# Desafio-2: Números Primos de 1 a 1000

## Objetivo
Este projeto tem como principal objetivo listar todos os números primos existentes no intervalo de 1 a 1000, implementando uma solução eficiente e didática em C++.

##  Fundamentação Teórica
A busca por números primos continua sendo um desafio fascinante na matemática computacional, com algoritmos cada vez mais eficientes sendo desenvolvidos para lidar com números grandes e complexos. Durante a resolução deste desafio, mergulhei em conceitos matemáticos que desconhecia, como o **Crivo de Eratóstenes**.

### O que é o Crivo de Eratóstenes?
Criado pelo matemático grego Eratóstenes de Cirene (276-194 a.C.), este método é uma maneira simples e prática para encontrar todos os números primos até um determinado limite. O algoritmo funciona eliminando sistematicamente os números compostos, "crivando" os primos.

## Solução Implementada

### Abordagem Escolhida
Embora o **Crivo de Eratóstenes** seja uma solução clássica com complexidade O(N log log N), optei por uma implementação mais didática baseada no seguinte recurso:

**Referência:** [Tutorial no YouTube](https://www.youtube.com/watch?v=xBbe2EOEsqs)

O vídeo apresenta uma abordagem simples e intuitiva para verificar se um número é primo, focando em:
- Validação de divisibilidade
- Otimização com raiz quadrada
- Casos especiais (números 0, 1 e 2)

### Estrutura do Código
O programa é composto por duas funções principais:
- `VerificandoEprimo(int n)`: Função que determina se um número específico é primo
- `ListarPrimos(int inicio, int fim)`: Função que itera de 1 a 1000 e exibe todos os números primos encontrados

## Como Compilar e Executar

### Pré-requisitos
Para compilar e executar este projeto em C++, você precisará ter instalado:
- Um compilador C++ (recomendados: g++ (GCC) 5.2.0, clang++, ou MSVC)
- Terminal ou prompt de comando

### Passos para Compilação

#### No Linux/Mac (com g++):
```bash
# Compilar o programa
g++ -o cpp main.cpp -std=c++11

# Executar
./cpp
