<?php

declare(strict_types=1);

final readonly class Primos
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
        $primos = [];

        for ($i = $this->limiteInicial; $i <= $this->limiteFinal; $i++) {
            if ($i < 2) {
                continue;
            }

            $primo = true;

            for ($divisor = 2; $divisor <= sqrt($i); $divisor++) {
                if ($i % $divisor === 0) {
                    $primo = false;
                    break;
                }
            }

            if ($primo) {
                $primos[] = $i;
            }
        }

        echo implode("\n", $primos);
    }
}