<?php
    for ($i = 1; $i <= 3010; $i++) {
        if (strval($i) == strval(strrev($i))) {
            echo $i . ' ';
        }
    }
?>