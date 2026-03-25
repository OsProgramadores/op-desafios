<?php
//Autor - William Garcia
//Executável - https://repl.it/JVaf/latest
$contP = 0;
$min = 3500;
$max = 3749;

echo "------Números Palindromos------\n";

for($min; $min <=$max;$min++){
  $inversao =strrev($min);
  if($inversao == $min){
    echo "{$min} é Palindromo\n";
    $contP++;
  }
}
echo "-------------------------------\n";
echo "Existem {$contP} números Palindromos entre {$min} e {$max}.\n";
?>



