defmodule PrimeNumbers do
  @moduledoc """
  Listing prime numbers.
  """

  @doc """
  PrimeNumbers.main/0 lists all prime numbers between 1 and 10000.

  ```
    iex> PrimeNumbers.main()
    {:ok,
      [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
      71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
      151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, ...]}
  ```
  """
  def main do
    primes(1, 10000)
    |> IO.inspect(limit: :infinity)
  end

  @doc """
  PrimeNumbers.primes/2 check for any prime numbers.

  ```
      iex> PrimeNumbers.primes(1, 10)
      {:ok, [2, 3, 5, 7]}
  ```
  """

  def primes(starting, ending) do
    result =
      Enum.to_list(starting..ending)
      |> Enum.filter(&is_prime?/1)

    {:ok, result}
  end

  def is_prime?(1), do: false
  def is_prime?(2), do: true
  def is_prime?(3), do: true

  @doc """
  PrimeNumbers.is_prime?/1 returns true when number is a prime number.

  ```
    iex> PrimeNumbers.is_prime?(974)
    false

    iex> PrimeNumbers.is_prime?(9973)
    true

  """
  def is_prime?(number) do
    2..floor(:math.sqrt(number))
    |> Enum.reduce_while(
      true,
      fn x, _acc ->
        if is_divisible_by?(number, x), do: {:halt, false}, else: {:cont, true}
      end
    )
  end

  defp is_divisible_by?(number1, number2), do: rem(number1, number2) == 0
end

PrimeNumbers.main()
