<?php

declare(strict_types=1);

final readonly class Primos
{
    public function __construct(private int $de, private int $ate)
    {
        if ($this->de > $this->ate) {
            throw new InvalidArgumentException('O valor inicial deve ser menor que o valor final');
        }

        if ($this->de < 0 || $this->ate < 0) {
            throw new InvalidArgumentException('Informe apenas números positivos');
        }

        $this->process();
    }

    private function process(): void
    {
        $primos = [];

        for ($i = $this->de; $i <= $this->ate; $i++) {
            if ($i < 2) {
                continue;
            }

            $primo = true;

            for ($divisor = 2; $divisor < $i; $divisor++) {
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