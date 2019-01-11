<?php

require_once('ReverseFile.php');

ini_set('memory_limit', '512M');

$start = microtime(true);

# informar o nome do arquivo como parâmetro
# exemplo: php main.php sample.txt
$arquivo = $argv[1];

if (!file_exists($arquivo)) {
    die("Arquivo não encontrado.\n");
}

$reverseFile = new ReverseFile($arquivo);
$reverseFile->execute();