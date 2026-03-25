defmodule PalindromesTest do
  use ExUnit.Case
  doctest Palindromes

  test "greets the world" do
    assert Palindromes.hello() == :world
  end
end
