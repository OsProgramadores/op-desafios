# Desafio 2: Números primos


## Proposta

Este programa é uma solução para o [Desafio #02](https://osprogramadores.com/desafios/d02/) proposto pelo grupo [OsProgramadores](https://osprogramadores.com/). Desenvolvido em Java, o código tem como propósito listar todos os números primos dentro do intervalo de 1 a 10000.

Para participar também dos desafios, visite a página em [osprogramadores.com/desafios](https://osprogramadores.com/desafios/) e confira todos os desafios.

## Como funciona o código?

A função `isPrime (int num)` recebe um número inteiro como parâmetro e verifica se é primo ou não. Se o número for primo, a função retorna `true`; caso contrário, retorna `false`, indicando que não é primo.

O loop `for (int i = 2; i <= 10000; i++)` varre cada número de 2 a 10000, passando-os à verificação da função `isPrime` para listar os números primos dentro deste intervalo. Os números primos são então impressos usando o comando `System.out.println(i)`, que exibe o resultado no console.

## Ferramentas Utilizadas

**Ambiente de Desenvolvimento Integrado (IDE):**

- **Eclipse**

O Eclipse foi escolhido como a IDE para o desenvolvimento deste desafio. Você pode baixar o Eclipse em [Baixar Eclipse](https://eclipseide.org).

**Kit de Desenvolvimento:**

- **Java 21**

Utilizei o Java 21 como Kit de Desenvolvimento para garantir compatibilidade e aproveitar as funcionalidades mais recentes da linguagem. Escolhi a versão 21 LTS , disponibilizada pela Azul (zulu) está disponível para download em: [Baixar Java 21](https://www.azul.com/downloads/?package=jre-fx#zulu).

## Como executar o código?

Para executar o código do desafio, é necessário ter as ferramentas mencionadas acima instaladas. Em seguida, abrir o arquivo no Eclipse e clicar em executar.
