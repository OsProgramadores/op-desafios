# Projeto: Números Primos entre 1 e 10000 em Java

Este é um projeto simples em Java que lista todos os números primos no intervalo de 1 a 10000 utilizando o algoritmo da "peneira de Eratóstenes".

## Descrição:
Os números primos são números naturais maiores que 1 e que possuem apenas dois divisores diferentes: 1 e o próprio número. O algoritmo da peneira de Eratóstenes é uma técnica eficiente para encontrar números primos em um determinado intervalo.

O projeto é escrito na linguagem Java e utiliza a IDE Eclipse para desenvolvimento e execução do código. Ele exibe uma lista de todos os números primos encontrados no intervalo de 1 a 10000.

## Como Funciona o Algoritmo?
1. Inicialmente, cria-se um array de booleanos chamado `numerosPrimos` de tamanho igual ao limite máximo do intervalo a ser verificado (10000 no nosso caso).
2. Define-se todos os valores do array como verdadeiros, assumindo que todos os números são primos.
3. Inicia-se um loop a partir do número 2 (primeiro número primo) até a raiz quadrada do limite (100 neste caso).
4. Para cada número primo encontrado no passo 3, marca-se todos os múltiplos desse número no array como falsos, pois eles são números compostos e não primos.
5. Ao final do algoritmo, todos os valores verdadeiros no array representam os números primos no intervalo.

## Como Executar o Projeto?
1. Instale o Java Development Kit (JDK) em sua máquina, caso ainda não o tenha feito.
2. Baixe e instale a IDE Eclipse, ou verifique se já a possui instalada em sua máquina.
3. Abra a IDE Eclipse e crie um novo projeto Java.
4. Copie o código fornecido no arquivo "ListaNumerosPrimos.java" deste repositório e cole-o em uma classe no projeto criado.
5. Execute a classe que contém o código do projeto clicando com o botão direito do mouse sobre o arquivo e selecionando "Run As" (Executar Como) -> "Java Application" (Aplicativo Java).
6. A saída do programa exibirá todos os números primos encontrados no intervalo de 1 a 10000.


