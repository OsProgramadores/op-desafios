defmodule PrimeNumbers do
  def main do
    primes(1, 10000)
  end

  def primes(starting, ending) do
    Enum.to_list(starting..ending)
    |> Enum.filter(&is_prime?/1)
    |> IO.inspect(limit: :infinity)
  end

  defp is_prime?(number) when number == 1, do: 1

  defp is_prime?(number) do
    result =
      Enum.to_list(2..(number - 1))
      |> Enum.reduce_while([], fn elem, acc -> stop_if_over_two(elem, acc, number) end)

    length(result ++ [1, number]) <= 2
  end

  defp stop_if_over_two(_elem, acc, _number) when length(acc) > 2, do: {:halt, acc}

  defp stop_if_over_two(elem, acc, number) when rem(number, elem) == 0,
    do: {:cont, acc ++ [elem]}

  defp stop_if_over_two(_elem, acc, _number), do: {:cont, acc}
end

PrimeNumbers.main()
