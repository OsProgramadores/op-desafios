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

    public function testNumbersWithOneDigit()
    {
        $result = (new Palindrome("1", "10"))->getPalindromes();
        $this->assertEquals(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            $result);
    }

    public function testInputsWereConvertedToInt()
    {
        $palindrome = new Palindrome("1.3", "8.9");
        $start = $palindrome->start;
        $end = $palindrome->end;

        $this->assertEquals(1, $start);
        $this->assertEquals(8, $end);
    }

    public function testSetCorrectlyTheSmallerAndBigger()
    {
        $p1 = new Palindrome("300", "100");

        $this->assertEquals(100, $p1->start);
        $this->assertEquals(300, $p1->end);

        $p2 = new Palindrome("1000", "999");

        $this->assertEquals(999, $p2->start);
        $this->assertEquals(1000, $p2->end);

        $p3 = new Palindrome("23", "32");

        $this->assertEquals(23, $p3->start);
        $this->assertEquals(32, $p3->end);
    }

    public function testSomeInputs()
    {
        $palindrome = new Palindrome("3000", "3010");
        $result = $palindrome->getPalindromes();

        $this->assertEquals(["3003"], $result);

        $palindrome = new Palindrome("101", "121");
        $result = $palindrome->getPalindromes();

        $this->assertEquals(["101", "111", "121"], $result);

        $palindrome = new Palindrome("1", "20");
        $result = $palindrome->getPalindromes();

        $this->assertEquals(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11"],
            $result);
    }

    public function testThrowIfOneArgWasNull()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("Informe os parâmetros necessários");
        new Palindrome("3000", null);

        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("Informe os parâmetros necessários");
        new Palindrome(null, "1234");
    }
}
