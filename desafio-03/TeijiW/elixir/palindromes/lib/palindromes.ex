defmodule Palindromes do
  def main() do
    starting = input("Start ")
    ending = input("End ")

    get_palindromes_list(starting, ending)
    |> IO.inspect(limit: :infinity)

    System.halt(0)
  end

  defp input(message), do: IO.gets(message) |> handle_input

  defp handle_input(input), do: String.to_integer(String.trim_trailing(input))

  def get_palindromes_list(starting, ending) do
    Enum.to_list(starting..ending)
    |> Enum.filter(&is_palindrome?/1)
  end

  def is_palindrome?(number) do
    number_string = to_string(number)
    if String.reverse(number_string) == number_string, do: true, else: false
  end
end

Palindromes.main()
