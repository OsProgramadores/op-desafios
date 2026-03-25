<?php
    for ($i = 1; $i <= 10000; $i++) {
        $primo = True;
        for ($j = 2; $j <= floor(sqrt($i)); $j++) {
            if ($i % $j == 0) {
                $primo = False;
            }
        }
        if ($primo) {
            echo $i . ' ';
        }
    }
?>