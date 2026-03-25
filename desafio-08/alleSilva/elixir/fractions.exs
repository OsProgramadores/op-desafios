defmodule Fraction do
  def transform_from_file(file) do
    file
    |> File.read!()
    |> String.split()
    |> Enum.each(& IO.puts(transform(&1)))
  end

  def transform(fraction) do
    fraction
    |> String.split("/")
    |> Enum.map(& String.to_integer/1)
    |> simplify()
  end

  def  mdc(m, 0), do: m

  def mdc(m, n) do
      mdc(n, rem(m, n))
  end

  def simplify([num]), do: "#{num}"

  def simplify([_, 0]), do: "ERR"

  def simplify([num, den]) do
    numerator = div(num, mdc(num, den))
    denominator = div(den, mdc(num, den))

    cond do
      mdc(numerator, denominator) == denominator -> "#{div(numerator, denominator)}"
      numerator < denominator -> "#{numerator}/#{denominator}"
      numerator > denominator -> "#{div(numerator, denominator)} #{rem(numerator, denominator)}/#{denominator}"
    end
  end
end

Fraction.transform_from_file("frac.txt")
