# 3: Palíndromos #

## Características ##

Implementação simples usando aritmética. Para um problema como esse, implementar com strings seria muito mais intuitivo, mas menos eficiente.
Visando modularidade, há uma função que faz o prompt e outra que faz o cálculo.

## helpers

* `main`: itera sobre o intervalo entre `initial/terminal` e imprime os palíndromos, tendo como helpers: 
  * `prompt_number`: recebe o input via stdin e retorna um `size_t`;
  * `is_palindrome`: faz o cálculo necessário para espelhar o número original e retorna um `bool` de acordo com a comparação entre as versões do número.


Do diretório raiz, compilar com `make palindromes` e executar com `./palindromes`.