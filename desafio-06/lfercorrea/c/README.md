# 6: Anagramas! #

*O exercício #06 tem complexidade fatorial. Já pode-se dizer que está na classe dos problemas de complexidade mais alta, sendo até pior do que os de complexidade exponencial. Do meu ponto de vista, isto é o que torna o desafio fascinante: você completa o exercício proposto, mas ele está muito longe de acabar só porque você resolveu em menos de 60 segundos...*

Neste código, o execício foi implementado em torno de tabelas de hash para acelerar a busca. Para um dicionario de 25 mil palavras em si, isto não é nem de longe necessário. O que importa é a diversão. Entretanto, contudo, porém, todavia, ainda falta usar a tabela para armazenar estados durante o backtracking para poupar estados já explorados. Embora isto ainda não tenha sido implementado, a gente chega lá.

## Características ##

Ao ler o arquivo `WORDS_TXT`, as palavras são lidas e filtradas em *load_file()*
com *viable_word()*, que faz uma subtração do token parametrizado de acordo com as contagens dos chars da palavra. As palavras rejeitadas nem entram na heap, o que já diminui consideravelmente o espaço de busca.

Foi adicionada a tabela `anagrams` com o propósito de melhorar a performance ao agrupar as palavras em anagramas. Nela, a estrutura é idêntica àquela de `dict`, exceto que aqui os anagramas não estão espalhados ao acaso pelos buckets. O hash de cada bucket aqui é gerado com base na palavra ordenada em vez da palavra bruta, como ocorria em *load_file()*. As colisões com os anagramas são tratadas, para além do encadeamento dos nós, posicionando dentro do vetor `words` naquele nó em vez de meramente adicionar no próximo, o que vai acelerar muito as buscas durante o backtracking (os testes feitos mostraram redução de 50~60% do tempo do algoritmo). A alocação das palavras também foi modularizada, sendo este um trabalho feito por *add_word()*.

O algoritmo de ordenação aplicado nas palavras foi *counting sort*, que é perfeito para a conveniente restrição de A-Z pelo exercício, portanto assintótico em O(n).

A função *create_hash()* é simples o bastante para fazer o trabalho de distinguir ABC de CBA com leveza. Entretanto, uma implementação com o *FNV-1a* seria tecnicamente muito mais apropriada para uso real, com tabelas mais populosas.

*"Cautela e caldo de galinha não fazem mal a ninguém, exceto à galinha!"* Por último, mas não menos importante, *unload_table()* libera toda a memória alocada nos nós. O código foi pensado de modo que a mesma função pudesse esvaziar tanto `anagrams` quanto `dict` da heap, e sua modularidade com a helper *unload_node()* facilita a integração de novas estruturas, se necessário.

O código está minimamente documentado. E, como dizem por aí: _"um código nunca está pronto"_.