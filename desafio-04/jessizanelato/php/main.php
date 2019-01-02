<?php

$pecasXadrez = [0 => ['total' => 0, 'desc' => 'Vazio'],
                1 => ['total' => 0, 'desc' => 'Peão'], 
                2 => ['total' => 0, 'desc' => 'Bispo'], 
                3 => ['total' => 0, 'desc' => 'Cavalo'], 
                4 => ['total' => 0, 'desc' => 'Torre'], 
                5 => ['total' => 0, 'desc' => 'Rainha'], 
                6 => ['total' => 0, 'desc' => 'Rei']];

# informar o nome do arquivo como parâmetro
# exemplo: php main.php sample_1.txt
$arquivo = $argv[1];

if (!file_exists($arquivo)) die("Arquivo não encontrado.\n");

$conteudo = file_get_contents($arquivo);

$tabuleiro = explode(PHP_EOL, $conteudo);

if(empty($tabuleiro)) die("Não há peças no tabuleiro a serem contadas.\n");

foreach ($tabuleiro as $linha) {
    $pecasDaLinha = explode(' ', $linha);
    foreach ($pecasDaLinha as $peca) {
        $pecasXadrez[$peca]['total']++;
    }
}

foreach ($pecasXadrez as $key => $peca) {
    if($key == 0) continue;
    echo $peca['desc'] . ": " . $peca['total'] . " peça(s)" . PHP_EOL;
}