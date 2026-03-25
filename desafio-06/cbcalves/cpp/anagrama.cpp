// Compilar com make ou: (caso não tenha clang++ usar g++)
// clang++ -Ofast anagrama.cpp -o anagrama -lm
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

class Anagramas
{
private:
    std::vector<std::string> _anagramas;
    std::vector<char *> _words;
    char *buffer;

    int is_anagrama(const char *s, const int *para_testar) // verifica se é anagrama (0) ou está no anagrama > 0
    {
        int testar[26], resp = 0;
        std::copy(&para_testar[0], &para_testar[26], &testar[0]);

        while (*s)
        {
            if (--testar[*s++ - 'A'] < 0)
                return -1;
        }
        for (auto &i : testar)
            resp += i;

        return resp;
    }
    void novo_teste(const char *s, const int *teste, int *n_teste) // construção de novo mapa, eliminando os caracteres da string
    {
        std::copy(&teste[0], &teste[26], &n_teste[0]);
        while (*s)
            n_teste[*s++ - 'A']--;
    }
    void combinar(const std::string &scomb_in, size_t i, int *sletras_in) // função recursiva de combinação de palavras até formar anagrama
    {
        int tmp = 0, sletras[26];
        std::string scomb;
        for (; i < _words.size(); i++)
        {
            if ((tmp = is_anagrama(_words[i], sletras_in)) < 0) // se não estiver no mapa vai pra próxima palavra
                continue;

            scomb = scomb_in + " " + _words[i];
            if (tmp == 0) // se o mapa retornou 0, significa q é uma palavra
                _anagramas.push_back(scomb);
            else
            {
                novo_teste(_words[i], sletras_in, sletras); // constrói novo mapa com as letras que faltam
                combinar(scomb, i + 1, sletras);
            }
        }
    }

public:
    ~Anagramas()
    {
        delete[] buffer;
    }
    void formar(const std::string &s)
    {
        std::fstream fs;
        size_t buffer_size = 0, novo_word_size = 0, palavra_size = 0;
        char *p = nullptr;
        char *novo_word = nullptr;
        int letras[26];

        palavra_size = s.length();
        for (auto &i : letras) // inicia o mapa com zeros
            i = 0;
        for (auto &i : s) // mapa das letras (não preciso da palavra)
            letras[i - 'A']++;

        fs.open("words.txt", std::fstream::in);
        if (!fs.is_open())
        {
            std::cout << "Arquivo não encontrado" << std::endl;
            return;
        }
        fs.seekg(0, fs.end);
        buffer_size = fs.tellg();
        fs.seekg(0, fs.beg);
        buffer = new char[buffer_size];
        if (!buffer)
        {
            std::cout << "Erro ao ler o arquivo" << std::endl;
            return;
        }
        fs.read(buffer, buffer_size);
        fs.close();

        p = buffer;
        while (*p)
        {
            novo_word = p;
            while (*p != '\n')
                p++;
            *p = 0;
            novo_word_size = p - novo_word;
            p++;
            if (novo_word_size == 0 || novo_word_size > palavra_size) // só entram no vetor palavras do tamanho ou menores que a inicial
                continue;
            if (is_anagrama(novo_word, letras) < 0) // só entram se estiverem contindas no mapa
                continue;
            _words.push_back(novo_word);
        }
        combinar("", 0, letras); // faz a combinação

        return;
    }

    size_t size() { return _anagramas.size(); }
    std::string &at(const size_t &index) { return _anagramas[index]; }
};

int main(int argc, char *argv[])
{
    size_t j = 0, i = 0;
    std::string palavra;
    Anagramas anagrama;

    if (argc < 2)
    {
        std::cout << "Uso: " << argv[0] << " <palavra ou \"frase\">" << std::endl;
        std::cout << "Com o máximo de 16 letras (sem contar espaços)" << std::endl;
        return 0;
    }

    palavra = argv[1];

    for (i = 0; i < palavra.length(); i++) // corta simbolos estranhos, espaços e transforma em maiúscula
    {
        if (palavra[i] >= 'a' && palavra[i] <= 'z')
            palavra[j++] = std::toupper(palavra[i]);
        else if (palavra[i] >= 'A' && palavra[i] <= 'Z')
            palavra[j++] = palavra[i];
    }
    palavra = palavra.substr(0, j); // reajusta o tamanho

    if (palavra.size() > 16) // verifica o tamanho da palavra resultado
    {
        std::cout << "Uso: " << argv[0] << " <palavra ou \"frase\">" << std::endl;
        std::cout << "Com o máximo de 16 letras (sem contar espaços)" << std::endl;
        return 0;
    }

    anagrama.formar(palavra); // formar os anagramas

    for (size_t i = 0; i < anagrama.size(); i++) // mostra o resultado
        std::cout << anagrama.at(i) << std::endl;

    return 0;
}