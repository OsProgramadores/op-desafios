# Desafio 2 : Primos

## Descrição
Implementei o algoritmo do Crivo de Eratóstenes para encontrar números primos com alta eficiência computacional.

## Contexto do Algoritmo

### Por que Crivo de Eratóstenes?

O Crivo de Eratóstenes é um método extremamente eficiente para identificar números primos em um intervalo. A principal vantagem está na sua abordagem de eliminação sistemática:

- Começa-se do primeiro número primo conhecido (2).
- Remove-se todos os seus múltiplos.
- Passa-se para o próximo número primo não eliminado.
- Repete-se o processo até a raiz quadrada do limite.

#### Exemplo Prático
Considerando números de 1 a 50:
1. Inicia-se com 2 (primeiro primo).
2. Remove múltiplos de 2: 4, 6, 8, 10, 12...
3. Próximo primo não eliminado: 3.
4. Remove múltiplos de 3: 6, 9, 12, 15...
5. Próximo primo: 5, 7, 11, 13...

### Lógica de Eliminação
- Não se passa por 4 porque seus múltiplos já foram removidos por 2.
- O algoritmo foca apenas nos primos: 2, 3, 5, 7, 11, 13...

## Funções Implementadas

### `isqrt(num)`
- **Objetivo**: Calcular a raiz quadrada inteira.
- **Entrada**: Número inteiro.
- **Saída**: Parte inteira da raiz quadrada.
- **Método**: Conversão eficiente para raiz quadrada inteira.

### `crivo(limit)`
- **Objetivo**: Gerar uma lista de números primos.
- **Entrada**: Limite máximo para busca.
- **Saída**: Lista de números primos até o limite.
- **Estratégia**:
  1. Criar lista inicial marcando todos como potencialmente primos.
  2. Eliminar múltiplos sistematicamente.
  3. Filtrar números primos restantes.

## Requisitos
- Python 3.x

## Modo de Uso

### Exemplo de Execução
```pycon
python d2.py
[2, 3, 5, 7 ... ]
