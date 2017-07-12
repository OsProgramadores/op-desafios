<?php
echo "---------NÚMEROS PRIMOS------------\n";

$limite = 1000;
$numDePrimos=0;
$cont = 0;

//https://repl.it/JUZS/6

for($n = 2;$n <=$limite;$n++){
  for($div = 1; $div <=$n; $div++){
    if($n % $div == 0)
    {
      $cont++;
    }
  }
  if($cont == 2){
    echo "Número {$n} é primo\n";
    $numDePrimos++;
  }
  $cont=0;
}
echo "------------------------------------\n";
echo "Existem {$numDePrimos} números primos até {$limite}";


?>