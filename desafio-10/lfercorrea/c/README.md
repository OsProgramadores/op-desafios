# 10: Turing machine

Implementação simples com três estruturas de dados para fita, regras e com dados do input.
O codigo foi escrito pensando na modularidade e legibilidade.

Não recebe argumento. O programa irá procurar na raiz o arquivo de dados *datafile* e fará a computação de cada input e seu respectivo **.tur*, desde que todos estejam no mesmo diretório. A fita é infinita, e o cabeçote inicia no meio dela, crescendo para qualquer lado.

No diretório raiz, compilar com `make turing` e rodar com `./turing`.

## helpers

* `main`
  * `compute`: processa a fita de acordo com as regras na heap;
  * `load_file`: carrega o arquivo de regras na heap e o input na stack;
  * `log_rule`: helper de load_file() que faz uma liked list com cada regra;
  * `lookup_rule`: procura uma regra que case, de acordo com o estado e a posicao do cabeçote na fita;
  * `print`: imprime a fita, delimitando as fronteiras manualmente, já que não existe '\0', antes de compute() possa liberar a fita da heap;
  * `realloc_tape`: garante a infinitude da fita;
  * `set_tape`: inicializa adequadamente a fita na heap;
  * `unload_llist`: limpa as regras da heap.
  