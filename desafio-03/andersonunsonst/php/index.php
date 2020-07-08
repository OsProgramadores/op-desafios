<?php

function isPalindrome($numberA, $numberB)
{
    for($numberA; $numberA < $numberB; $numberA++) {

	    if(strrev($numberA) == $numberA) {
		    echo $numberA . PHP_EOL;
	    }

    }

}

isPalindrome(1, 1000);

?>