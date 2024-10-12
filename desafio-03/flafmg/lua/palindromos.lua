function eh_palindromo(num)
    local str_num = tostring(num)
    local str_reversa = string.reverse(str_num)
    return str_num == str_reversa
end

function imprimir_palindromos(inicio, fim)
    for i = inicio, fim do
        if eh_palindromo(i) then
            io.write(i .. " ")
        end
    end
    print()
end

print("digite o numero inicial:")
local inicio = tonumber(io.read())
print("digite o numero final:")
local fim = tonumber(io.read())

imprimir_palindromos(inicio, fim)
