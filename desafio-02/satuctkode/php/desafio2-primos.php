<?php
    // Realizando 10000 repetições.
    for($numero = 1; $numero <= 10000; $numero++){
        // Essas variáveis serão resetadas a cada loop completo no laço 'for'.
        $contagem = 1;
        $qtd_divisores = 0;

        // Aqui será feito uma contagem de 1 até o numero atual do laço 'for'.
        // Após o inicio da contagem, será verificado se o número atual da contagem dividido pelo numero atual do laço 'for' é igual a 0, se sim, será feito as seguintes verificações:
        // * Se o número atual da contagem é igual a 1, a variável de quantidade de divisores receberá + 1.
        // * Se o número atual da contagem é diferente do número atual do laço 'for', o laço 'while' do número atual da contagem será quebrado(break) e a contagem avançará para o próximo número(se existir).
        // * Se caso o while não for quebrado pelo break, será verificado se o número atual da contagem é igual ao número atual do laço 'for', se sim, a variável de quantidade de divisores receberá + 1.
        while($contagem <= $numero){
            if($numero % $contagem == 0){
                if($contagem == 1){
                    $qtd_divisores++;
                }else if($contagem != $numero){
                    break;
                }else if($contagem == $numero){
                    $qtd_divisores++;
                }
            }

            $contagem++;
        }

        // Se a quantidade de divisores do número atual do laço 'for' é igual a 2, esse número será mostrado.
        if($qtd_divisores == 2){
            echo $numero." ";
        }
    }
?>