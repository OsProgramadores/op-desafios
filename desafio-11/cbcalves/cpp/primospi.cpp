#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

#define ORGANIZE 10000 // a cada ORGANIZE em primos eu vejo a maior sequencia e apago o vetor de primos

class Primos // classe para calcular e guardar todos os primos de 2 até 9973
{
private:
    std::vector<int> primos;

public:
    Primos() // usando o desafio 02 para formar os primos até 9973
    {
        size_t j = 0;
        primos.reserve(1229); // numero de primos até 9973
        primos.resize(4);
        primos[0] = 2;
        primos[1] = 3;
        primos[2] = 5;
        primos[3] = 7;
        // O passo é de 2 em 2 para testar apenas números impares
        for (int i = 11; i < 9974; i += 2)
        {
            // Ganho de velocidade.
            if ((i % 5) == 0 || (i % 3) == 0)
                continue;
            for (j = 3; j < primos.size(); j++)
            {
                // Se não for primo o resto é zero.
                if ((i % primos[j]) == 0)
                    break;
                // Se o resultado for menor que o divisor, quer dizer que
                // não tem um primo que multiplicando por outro primo menor
                // de o número, ele é primo, não vou até o fim da array.
                if ((i / primos[j]) < primos[j])
                {
                    j = primos.size();
                    break;
                }
            }
            if (j == primos.size())
                primos.push_back(i);
        }
    }
    bool is_primo(char *s) // verifica a existência do número na lista de primos.
    {
        std::vector<int>::iterator it;
        it = std::find(primos.begin(), primos.end(), std::stoi(s));
        if (it != primos.end()) // se estiver na lista é primo
            return true;

        return false;
    }
};

namespace primespi
{
    struct pi_primes_t // estrutura que guarda os primos e a posição deles em pi
    {
        char *start;
        char *end;
        pi_primes_t() : start(nullptr), end(nullptr) {}             // inicialização das variáveis
        void set(char *s, char *e) { start = s, end = e; }          // entrada de dados
        bool operator<(pi_primes_t B) { return (start < B.start); } // comparação para sort pela posição em pi
    };
    pi_primes_t max;

    char *maior_seq_r(const std::vector<pi_primes_t> &pi, char *in_end, size_t i)
    {
        char *maior = in_end, *resp = nullptr;

        for (; i < pi.size(); i++)
        {
            if ((in_end + 1) < pi[i].start) // como está em ordem de início, se o início ficou mais alto que o final procurado, não existe mais sequencia
                break;
            if ((in_end + 1) == pi[i].start) // se o início é igual ao final, aumenta a sequencia para verificar
            {
                resp = maior_seq_r(pi, pi[i].end, i + 1);
                if (maior < resp)
                    maior = resp;
            }
        }
        return maior;
    }

    void maior_seq(std::vector<pi_primes_t> &pi) // forma as sequencias de primos
    {
        char *resp = nullptr;
        for (size_t i = 0; i < pi.size(); i++)
        {

            resp = maior_seq_r(pi, pi[i].end, i + 1);
            if ((max.end - max.start) < (resp - pi[i].start))
            {
                max.end = resp;
                max.start = pi[i].start;
            }
        }
        pi.clear();
        pi.push_back(max);
    }

} // namespace primespi

int main()
{
    std::fstream fs;
    char *c = nullptr, *buffer = nullptr;
    size_t buffer_size = 0;
    char s1[2] = {0, 0}, s2[3] = {0, 0, 0}, s3[4] = {0, 0, 0, 0}, s4[5] = {0, 0, 0, 0, 0};
    std::vector<primespi::pi_primes_t> pi_primes;
    primespi::pi_primes_t pi_primes_insert;
    Primos primos;

    fs.open("pi-1M.txt", std::fstream::in);
    if (!fs.is_open())
    {
        std::cout << "Arquivo não encontrado" << std::endl;
        exit(1);
    }
    fs.seekg(0, std::fstream::end);
    buffer_size = fs.tellg(); // tamanho do arquivo
    fs.seekg(0, std::fstream::beg);

    buffer = new char[buffer_size + 1];
    if (!buffer)
    {
        std::cout << "Memória insuficiente para abrir o arquivo" << std::endl;
        fs.close();
        exit(1);
    }
    fs.read(buffer, buffer_size);
    fs.close();
    c = buffer;

    pi_primes.reserve(ORGANIZE + 4);

    while (*c != '.') // pular o '3.'
        c++;
    c++;

    std::cout << std::setw(3) << 0 << "%" << std::flush;
    while (*c) // após o . vai até não ter mais entradas
    {
        s1[0] = *c;                                              // 1 número
        s2[0] = s2[1], s2[1] = *c;                               // 2 números
        s3[0] = s3[1], s3[1] = s3[2], s3[2] = *c;                // 3 números
        s4[0] = s4[1], s4[1] = s4[2], s4[2] = s4[3], s4[3] = *c; // 4 números

        if (primos.is_primo(s1))
        {
            pi_primes_insert.set(c, c);
            pi_primes.push_back(pi_primes_insert);
        }
        if (s2[0] && primos.is_primo(s2)) //maior que 0 garante que o [0] está preenchido
        {
            pi_primes_insert.set(c - 1, c);
            pi_primes.push_back(pi_primes_insert);
        }
        if (s3[0] && primos.is_primo(s3))
        {
            pi_primes_insert.set(c - 2, c);
            pi_primes.push_back(pi_primes_insert);
        }
        if (s4[0] && primos.is_primo(s4))
        {
            pi_primes_insert.set(c - 3, c);
            pi_primes.push_back(pi_primes_insert);
        }

        if (ORGANIZE < pi_primes.size()) // quando a variavel atinge "ORGANIZE" entradas, reorganizar e deixar a maior entrada
        {
            std::cout << "\b\b\b\b" << std::setw(3) << ((c - buffer) / 10000) << "%" << std::flush;
            std::sort(pi_primes.begin(), pi_primes.end()); //sort pelo índice de inicio.
            primespi::maior_seq(pi_primes);
        }
        c++;
    }
    std::cout << "\b\b\b\b" << std::setw(3) << 100 << "%" << std::flush;
    std::sort(pi_primes.begin(), pi_primes.end()); //sort pelo índice de inicio.
    primespi::maior_seq(pi_primes);

    *++primespi::max.end = 0;
    std::cout << "\b\b\b\b" << primespi::max.start << std::endl; // mostrar o numero

    delete[] buffer;
    return 0;
}
