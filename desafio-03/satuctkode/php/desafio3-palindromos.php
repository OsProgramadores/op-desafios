<?php
$inicio_contagem = 1;
$fim_contagem = 100;
$valor_inicial = 0;
$valor_final = [];

// Realizando a contagem de um número inicial a um número final
for($num = $inicio_contagem; $num <= $fim_contagem; $num++){
    // Convertendo o número atual de int para string e colocando ele em uma variável
    $valor_inicial = strval($num);

    // O script dentro do 'if' só será executado se o comprimento do número atual for maior que 1
    // Se não, será mostrado os números de apenas um dígito
    if(strlen($valor_inicial) > 1){
        // Passando dígito por dígito para um array, no final disso o array vai ter um número reverso ao número atual
        for($chave = 0; $chave < strlen($valor_inicial); $chave++){
            array_unshift($valor_final, $valor_inicial[$chave]);
        }

        // O resultado só será mostrado se o número atual for igual ao número reverso
        if($valor_inicial == implode($valor_final)){
            echo intval($valor_inicial)." ";
        }

        // Resetando o array
        $valor_final = [];
    }else{
        echo $num." ";
    }
}
?>