<?php

function isPrime($num) {
    if ($num < 2) {
        return false;
    }

    for ($i = 2; $i <= sqrt($num); $i++) {
        if ($num % $i == 0) {
            return false;
        }
    }

    return true;
}

for ($num = 2; $num <= 10000; $num++) {
    if (isPrime($num)) {
        echo "{$num}" . PHP_EOL;
    }
}

?>
