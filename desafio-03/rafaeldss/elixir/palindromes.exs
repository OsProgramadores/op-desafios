{inicio, _} = IO.gets("") |> Integer.parse
{fim, _} = IO.gets("") |> Integer.parse


Enum.each(inicio..fim, fn(number) ->
  num = Integer.to_string(number)

  if num == String.reverse(num) do
    IO.puts(number)
  end
end)
