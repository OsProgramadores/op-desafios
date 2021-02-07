defmodule PrimeNumbersTest do
  use ExUnit.Case
  doctest PrimeNumbers

  test "greets the world" do
    assert PrimeNumbers.hello() == :world
  end
end
