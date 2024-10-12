function eh_primo(n)
    if n < 2 then return false end
    for i = 2, math.sqrt(n) do
        if n % i == 0 then
            return false
        end
    end
    return true
end

for i = 1, 10000 do
    if eh_primo(i) then
        print(i)
    end
end