<?php

namespace Test;

use App\Palindrome;
use InvalidArgumentException;
use PHPUnit\Framework\TestCase;

final class PalindromeTest extends TestCase
{
    public function testArgsArentInts()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("Parâmetros devem ser números inteiros");
        new Palindrome("bar", "foo");
    }

    public function testArgsAreBiggerThan0()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("Parâmetros devem ser maiores que 0");
        new Palindrome("0", "-1");
    }

    public function testEnsureArgIsInt()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("Parâmetros devem ser inteiros");
        new Palindrome("14", "7.7");
    }
}
