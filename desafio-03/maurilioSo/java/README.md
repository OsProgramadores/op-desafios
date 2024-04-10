# Desafio 3: Números palindrômicos


## Proposta

Este programa é uma solução para o [Desafio #03](https://osprogramadores.com/desafios/d02/) proposto pelo grupo [OsProgramadores](https://osprogramadores.com/). Desenvolvido em Java, o código tem como propósito listar todos os números palindromicos dentro do intervalo de 1 a 100000.

Para participar também dos desafios, visite a página em [osprogramadores.com/desafios](https://osprogramadores.com/desafios/) e confira todos os desafios.

## Como funciona o código?

O programa tem dois métodos auxiliar para solucionar o desafio: 
O `toString(int num_s)` Este método converte um número inteiro em sua representação de string, invertendo os dígitos no processo.
O `ehPalidromico(String a, int num)`: Verifica se a string reversa de um número é igual ao próprio número, retornando verdadeiro se for o caso.


O meétodo `Main()` O método principal do programa que itera de 1 a 100000 e imprime os números palindrômicos encontrados utilizando os métodos `toString(int num_s)` e `ehPalidromico(String a, int num)`.
## Ferramentas Utilizadas

**Ambiente de Desenvolvimento Integrado (IDE):**

- **Eclipse**

O Eclipse foi escolhido como a IDE para o desenvolvimento deste desafio. Você pode baixar o Eclipse em [Baixar Eclipse](https://eclipseide.org).

**Kit de Desenvolvimento:**

- **Java 21**

Utilizei o Java 21 como Kit de Desenvolvimento para garantir compatibilidade e aproveitar as funcionalidades mais recentes da linguagem. Escolhi a versão 21 LTS , disponibilizada pela Azul (zulu) está disponível para download em: [Baixar Java 21](https://www.azul.com/downloads/?package=jre-fx#zulu).

## Como executar o código?

Para executar o código do desafio, é necessário ter as ferramentas mencionadas acima instaladas. Em seguida, abrir o arquivo no Eclipse e clicar em executar.

## Notas:
Este script foi projetado para encontrar números palindrômicos no intervalo de `1 a 100000`. Você pode ajustar o intervalo conforme necessário alterando os limites no loop for no método main().
Este programa é uma implementação simples e direta para encontrar números palindrômicos. Para intervalos maiores ou otimizações adicionais, podem ser necessárias abordagens diferentes.