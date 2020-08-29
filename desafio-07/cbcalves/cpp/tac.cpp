// compilar como :
// g++ -Ofast tac.cpp -o tac
//
#include <fstream>
#include <iostream>

#define BUFFER_SIZE 104857600 // 100MB = 1024 * 1024, o limite são 500MB

int main(int argc, char *argv[])
{
    std::fstream fs;
    size_t p = 0, size = 0, last = 0;
    char *buffer = nullptr;

    if (argc < 2)
    {
        std::cout << "Uso: " << argv[0] << " <arquivo>" << std::endl;
        return 0;
    }
    fs.open(argv[1], std::fstream::in);
    if (!fs.is_open())
    {
        std::cout << "Arquivo não encontrado" << std::endl;
        abort();
    }

    fs.seekg(0, std::fstream::end);
    size = fs.tellg(); // tamanho do arquivo

    while (size)
    {
        if ((size + last) < BUFFER_SIZE) // se tiver algo no buffer que não foi impresso ele tenta fechar a linha de novo
        {
            if (buffer)
                delete[] buffer;
            fs.seekg(0, std::fstream::beg);
            buffer = new char[(size + last)];
            if (!buffer)
            {
                std::cout << "Erro de alocação, memória insuficiente para executar o programa" << std::endl;
                break;
            }
            fs.read(buffer, (size + last));
            size = 0;
        }
        else
        {
            if (buffer)
                delete[] buffer;
            size = (size + last) - BUFFER_SIZE;
            buffer = new char[(BUFFER_SIZE + 1)];
            if (!buffer)
            {
                std::cout << "Erro de alocação, memória insuficiente para executar o programa" << std::endl;
                break;
            }
            fs.seekg(size, std::fstream::beg);
            fs.read(buffer, BUFFER_SIZE);
        }
        p = fs.gcount();
        buffer[p] = 0;
        p -= 1;
        do
        {
            p--;
            if (buffer[p] == '\n') // quando encontra '\n' ele imprime o buffer a partir da posição p+1
            {
                std::cout << &buffer[p + 1] << std::flush;
                buffer[p + 1] = 0; // esse 0 é para na próxima impressão não ter a parte já mostrada
                last = p + 1;
            }
        } while (p > 0);
    }
    if (buffer) // se o buffer não estiver vazio ele imprime
    {
        std::cout << buffer << std::flush;
        delete[] buffer;
    }

    return 0;
}
