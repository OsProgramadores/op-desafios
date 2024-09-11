<?php
$start = 1;
$end = 20;

for ($i = $start; $i <= $end; $i++) {
    if (strval($i) === strrev($i)) {
        echo "{$i}" . PHP_EOL;
    }
}
