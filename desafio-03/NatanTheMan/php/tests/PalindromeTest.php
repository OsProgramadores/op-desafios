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
}
