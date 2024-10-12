function createFileWithLines(lineCount)
    local fileName = "test.txt"
    local file = io.open(fileName, "w")

    if not file then
        print("erro criando arquivo")
        return
    end

    for i = 1, lineCount do
        file:write("linha muito legal " .. i .. "\n")
    end

    file:close()
    print("arquivo criado " .. fileName)
end

io.write("numero de linhas ")
local lineCount = tonumber(io.read())

if lineCount and lineCount > 0 then
    createFileWithLines(lineCount)
else
    print("invalid")
end
