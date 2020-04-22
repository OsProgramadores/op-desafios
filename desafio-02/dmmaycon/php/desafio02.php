<?php

/**
 * Desafios 
 * #2: PRIMOS 
 * 
 * Description: 
 * Listando n�meros primos, escreva um programa para listar todos os n�meros primos entre 1 e 10000
 * 
 * Disclaimer: Como o desafio tem um n�mero limite resolvi utilizar o 
 * Crivo de Erast�steles (https://pt.wikipedia.org/wiki/Crivo_de_Erat�stenes)
 * para encontrar os n�meros primos.
 * 
 * Rodar tanto via CLI ou Browser
 * 
 * Author: Maycon de Moraes
 * Date: 22/04/2020
 */


/**
 * Chamada do programa
 */
function main() : void {
    
    $limite = 10000;
    $raizLimite = round(sqrt($limite));
    $lista  = [];

    // popula a lista inicial
    for ($i = 2; $i <= $limite; $i++) {
        $lista[] = $i;
    }
    
    $controle = $lista[0]; // primeiro n�mero do array
    while ($controle <= $raizLimite) {
        $lista = array_filter($lista, function ($item) use ($controle) {
            if ($item % $controle == 0 && $item != $controle) {
                return false; // retira os multiplos da lista
            }
            return true;
        });
        $controle++;
    }

    // imprime a lista de primos
    print_r($lista);
}

main();

