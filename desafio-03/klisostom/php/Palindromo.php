<?php

class Palindromo
{
    private function ehPalindromo(int $numero): bool
    {
        return strrev("".$numero) == $numero;
    }

    public function listarEntreDoisNumeros(int $numeroX, int $numeroY): array
    {
        $achados = [];

        for ($i=$numeroX; $i <= $numeroY; $i++) {
            if ($this->ehPalindromo($i)) {
                $achados[] = $i;
            }
        }

        return $achados;
    }
}
