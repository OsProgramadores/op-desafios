Implementeção muito interessante, primeiro o algoritmo testava todas as palavras da lista, se achasse uma que se encaixa na sentenca , excluia as letras em comum e continuava a busca.

A segunda implementação ordenava as palavras por tamanho e só pesquisava até que aquelas de tamanho igual ao que restou dasentença.

A terceira implementação quando encontrava uma palavra , procurava a seguinte a partir da seguinte no dicionário já que as anteriores já havian sido procuradas.

A quarta implementação permitiu alcançar a meta de 60 segundos proposta pelo desafio. Neste código foi usado um segundo dicionário filtrado com apenas palabras contidas no input, assim restringimos absurdamente a quantidade de palavras e serem pesquisadas.

A quinta permitiu alcançar um tempo de execução de menos de 15 segundos, nesta implementação foi criado um novo dicionário para cada nova interação da função search() . Esse dicionário inicialmente alocaria as palavras filtradas em um novo array, porém uma abordagem mais eficiente acabou sendo armazenar apenas os ponteiros para as palavras já carregadas, nesse caso não se perderia tempo alocando memória assim como economizamos memória, já que as palavras em si já estavam carregadas.


