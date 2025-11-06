<?php

namespace Test;

use App\Palindrome;
use InvalidArgumentException;
use PHPUnit\Framework\TestCase;

final class PalindromeTest extends TestCase
{
    public function testArgsAreInts()
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage("Parâmetros devem ser números inteiros");
        new Palindrome("bar", "foo");
    }

    public function testArgsAreBiggerThan0()
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage("Parâmetros devem ser maiores que 0");
        new Palindrome("0", "-1");
    }
}
