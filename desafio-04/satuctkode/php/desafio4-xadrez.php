<?php
    $pecas = array(
                    1 => "Peão",
                    2 => "Bispo",
                    3 => "Cavalo",
                    4 => "Torre",
                    5 => "Rainha",
                    6 => "Rei"
    );

    $tabuleiro_exemplo1 = array(
                                0 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                1 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                2 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                3 => array("0", "0", "0", "1", "1", "0", "0", "0"),
                                4 => array("0", "0", "0", "1", "1", "0", "0", "0"),
                                5 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                6 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                7 => array("0", "0", "0", "0", "0", "0", "0", "0")
    );

    $tabuleiro_exemplo2 = array(
                                0 => array("4", "3", "2", "5", "6", "2", "3", "4"),
                                1 => array("1", "1", "1", "1", "1", "1", "1", "1"),
                                2 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                3 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                4 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                5 => array("0", "0", "0", "0", "0", "0", "0", "0"),
                                6 => array("1", "1", "1", "1", "1", "1", "1", "1"),
                                7 => array("4", "3", "2", "5", "6", "2", "3", "4")
    );

    // Enquanto o código da peça atual for menor que 7, será feito verificações em cada linha de um tabuleiro, em cada verificação de uma linha vai ser somado a quantidade de peças com o código atual, logo após essa soma será mostrado a quantidade da peça atual. Isso será repetido linha por linha até o final do tabuleiro.
    $codigo_peca_atual = 1;
    while($codigo_peca_atual < 7){
        $total_peca_atual = 0;
        foreach($tabuleiro_exemplo2 as $linha){
            $total_peca_atual += count(array_keys($linha, $codigo_peca_atual));
        }      
        echo "<strong>".$pecas[$codigo_peca_atual].":</strong> ".$total_peca_atual." peça(s)<br>";
        $codigo_peca_atual++;
    }
?>