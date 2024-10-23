# Desafio 03: Palindromos
Solução implementada sem uso de conversão pra string :).

## Sobre a solução
Primeiro defini a função que faz a verificação do número que é recebido por parâmetro, e retorna um `bool`, `True` caso seja palindromo e `False` caso não.

Já no escopo da função defini duas variáveis, `number_copy` que cria uma cópia do número original que vai ser usada para gerar o numero reverso sem ter que mexer no número original e `number_reverse` que vai ser o número reverso.

> para escrever um numero ao contrario matematicamente primeiro usasse a operação `mod (%)`, que pega o numero, divide por **10** e o resto é exatamente o ultimo digito do número.
> depois que extrair o ultimo digito, usa a variável `number_reverse` pra criar o numero ao contrário, digito por digito. pegando o valor atual multiplicando por **10** e somando com o ultimo digito extraido.
> agora, pegamos a copia do numero original (`number_copy`) e removemos o ultimo digito usando divisão inteira (`//` no python).

Ao final do laço e no fim da função verificamos se o numero invertido (`number_reverse`) é igual a o número original, caso seja, a operação retornará `True` iformando que é palindromo.

Agora é so chamar a função usando um `loop` do *número incial* (`first_number`) ate o *ultimo numero* (`last_number`) e verificar cada numero do laço passando como argumento na chamada da função, assim imprimindo-o caso retorne `True`.
