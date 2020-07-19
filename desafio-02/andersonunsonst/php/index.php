<?php

function primeCheck($number)
{
    if ($number == 1) {
        return 0; 
    }   
      
    for ($i = 2; $i <= sqrt($number); $i++) {
        if ($number % $i == 0) {
            return 0; 
        }
    }

    return 1; 
}


function printPrime($min, $max)
{
    for($min; $min < $max; $min++) {
        if(primeCheck($min)==1) {
            echo $min . PHP_EOL;
        }
    }
}


printPrime(1, 10000);

?>
