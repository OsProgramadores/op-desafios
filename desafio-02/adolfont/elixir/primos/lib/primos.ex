defmodule Primos do
  @moduledoc """
  Primos verifica se um número é primo
  """

  @doc """
  is_prime?(number) returns true when number is a prime number

  """
  def is_prime?(1), do: false
  def is_prime?(2), do: true
  def is_prime?(3), do: true

  def is_prime?(number) do
    2..floor(:math.sqrt(number))
    |> Enum.reduce_while(
      true,
      fn x, _acc ->
        if is_divisible_by?(number, x), do: {:halt, false}, else: {:cont, true}
      end
    )
  end

  defp is_divisible_by?(num1, num2) do
    rem(num1, num2) == 0
  end

  defp all_primes_between(start, ending) when start <= ending do
    start..ending
    |> Enum.map(&{&1, is_prime?(&1)})
    |> Enum.filter(fn {_x, y} -> y end)
    |> Enum.map(fn {x, _y} -> x end)
  end

  def main() do
    IO.puts("Todos os números primos entre 1 e 10000")

    all_primes_between(1, 10000)
    |> Enum.map(&IO.puts(&1))
  end
end

Primos.main()
