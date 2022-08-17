<?php

namespace Klisostom\Php;

class ListandoPrimosEntreUmEDezMil
{
    public function listar(int $maxValue): array
    {
        $foundPrimes = [2];
        $index = 3;

        while (
            $foundPrimes[count($foundPrimes) - 1] < $maxValue &&
            $index < $maxValue
        ) {
            if ($this->ehImpar($index)) {
                $ehPrimo = true;

                for ($z = 2; $z < $index; $z++) {
                    if ($index % $z === 0) {
                        $ehPrimo = false;
                        break;
                    }
                }

                if ($ehPrimo) {
                    $foundPrimes = [...$foundPrimes, $index];
                }
            }

            $index++;
        }

        return $foundPrimes;
    }

    private function ehImpar(int $number): bool
    {
        return $number % 2 !== 0;
    }
}
