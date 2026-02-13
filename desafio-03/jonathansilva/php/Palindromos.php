<?php

declare(strict_types=1);

final readonly class Palindromos
{
    public function __construct(private int $limiteInicial, private int $limiteFinal)
    {
        if ($this->limiteInicial > $this->limiteFinal) {
            throw new InvalidArgumentException('O valor inicial deve ser menor que o valor final');
        }

        if ($this->limiteInicial < 0 || $this->limiteFinal < 0) {
            throw new InvalidArgumentException('Informe apenas números positivos');
        }
    }

    public function process(): void
    {
        $palindromos = [];

        for ($i = $this->limiteInicial; $i <= $this->limiteFinal; $i++) {
            $numeroComoString = strval($i);
            $numeroRevertido = strrev($numeroComoString);

            if ($numeroComoString === $numeroRevertido) {
                $palindromos[] = $i;
            }
        }

        echo implode(", ", $palindromos);
    }
}