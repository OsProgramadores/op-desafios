defmodule PowerOfTwo do
  def exec do
    File.read!("numbers.txt")
    |> String.split()
    |> Enum.map(& String.to_integer/1)
    |> Enum.each(& IO.inspect(power_of_two(&1)))
  end

  def power_of_two(num), do: divide_by_two(num, num, 0)
  def power_of_two(0, _, _), do: "0 false"
  #def power_of_two(1, _, _), do: "2 true 1"
  def divide_by_two(num, 0, acc2), do: "#{num} true #{acc2}"
  def divide_by_two(num, acc1, acc2) do
    acc2 = acc2 + 1
    if rem(acc1, 2) == 0 do
      acc1 = div(acc1, 2)
      divide_by_two(num, acc1, acc2)
    else
      "#{num} false"
    end
  end
end

PowerOfTwo.exec()
