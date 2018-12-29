<?php

final class NumerosPrimos {
    
    public static function encontrarNumerosPrimos ($inicio = 1, $limite) {

        $numerosPrimos = [];

        for($num = $inicio; $num <= $limite; $num++){

            $divisores = self::encontrarDivisores($num);
        
            if(count($divisores) == 1) {
                $numerosPrimos[] = $num;
            }
            
        }

        return $numerosPrimos;
    }

    private static function encontrarDivisores($numero) {
        $divisor = 2;
        $divisores = [];

        while($numero > 1) {
            while ($numero % $divisor == 0) {
                $numero = $numero / $divisor;
                $divisores[] = $divisor;
            }
            $divisor++;
        }

        return $divisores;
    }

}