<?php

$definicaoPedrasXadrez = [1 => 'Peão', 2 => 'Bispo', 3 => 'Cavalo', 4 => 'Torre', 5 => 'Rainha', 6 => 'Rei'];

# informar o nome do arquivo como parâmetro
# exemplo: php main.php sample_1.txt
$arquivo = $argv[1];

if (!file_exists($arquivo)) {
    die("Arquivo não encontrado.\n");
}

$aberturaArquivo = fopen($arquivo, "r");
$conteudo = fread($aberturaArquivo, filesize($arquivo));
fclose($aberturaArquivo);

$tabuleiro = explode(PHP_EOL, $conteudo);

if(empty($tabuleiro)) die("Não há peças no tabuleiro a serem contadas.\n");

$pecas = [];

foreach ($tabuleiro as $linha) {
    $pecasDaLinha = explode(' ', $linha);
    foreach ($pecasDaLinha as $peca) {
        $peca = (int) $peca;
        $peca = $peca > 0 && $peca < 7 ? $peca : 0;
        if(!isset($pecas[$peca])) $pecas[$peca] = 0;
        $pecas[$peca]++;
    }
}

foreach ($definicaoPedrasXadrez as $codigo => $descricao) {
    $totalPecas = isset($pecas[$codigo]) ? $pecas[$codigo] : 0;
    echo "{$descricao}: {$totalPecas} peça(s)\n";
}