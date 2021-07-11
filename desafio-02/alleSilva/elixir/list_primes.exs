defmodule ListPrimes do
  def call() do
    2..10_000
    |> Enum.filter(&is_prime/1)
    |> Enum.each(&IO.inspect/1)
  end

  def is_prime(num) when num > 0, do: verify_rem(num, 1)
  defp verify_rem(n, n), do: true

  defp verify_rem(n, acc) do
    acc = acc + 1
    root = :math.sqrt(n)
    if acc <= root && rem(n, acc) == 0 do
      false
    else
      verify_rem(n, acc)
    end
  end
end

ListPrimes.call()
