<?php

declare(strict_types=1);

namespace Test;

use App\Palindrome;
use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\Attributes\Test;

final class PalindromeTest extends TestCase
{
    #[Test]
    public function assertArgsAreInts()
    {
        $this->expectException(InvalidArgumentException::class);
        new Palindrome("bar", "foo");
    }

    #[Test]
    public function assertArgsAreBiggerThan0()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("Parâmetros devem ser maior que 0");
        new Palindrome("0", "-1");
    }
}
