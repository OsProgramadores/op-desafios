defmodule PrimosTest do
  use ExUnit.Case

  test "1 is not prime" do
    assert not Primos.is_prime?(1)
  end

  test "2 is prime" do
    assert Primos.is_prime?(2)
  end

  test "3 is prime" do
    assert Primos.is_prime?(3)
  end

  test "see all prime numbers between 1 and 20" do
    primes_1_20 =
      1..20 |> Enum.map(&{&1, Primos.is_prime?(&1)}) |> Enum.filter(fn {_x, y} -> y end)

    answer = [
      {2, true},
      {3, true},
      {5, true},
      {7, true},
      {11, true},
      {13, true},
      {17, true},
      {19, true}
    ]

    assert primes_1_20 == answer
  end
end
