#include <algorithm>
#include <iostream>
#include <thread>
#include <vector>

#define MAX_THREADS 300 // máximo de threads (se subir muito o número e o computador não aguentar, vai ficar lento)
#define ORGANIZE 10000  // a cada ORGANIZE em primos eu vejo a maior sequencia e apago parte do veto de primos

#define DELETE(ptr)     \
    if (ptr != nullptr) \
    delete ptr, ptr = nullptr // defini esse DELETE para evitar problemas de acesso ao apagar ponteiros

struct Pi_Primes //estrutura que guarda os primos e a posição deles em pi
{
    int start, end;
    std::string number;
    Pi_Primes() : start(INT32_MAX), number(""), end(INT32_MAX) {}       //inicialização da variável
    void set(int i, char *s, int e) { start = i, number = s, end = e; } //entrada de dados
    bool operator<(Pi_Primes B) { return (start < B.start); }           // comparação para sort pela posição em pi
};

class Primos // classe para calcular e guardar todos os primos de 2 até 9973
{
private:
    std::vector<int> primos;

public:
    Primos() : primos(4) //usando o desafio 02 para formar os primos até 9973
    {
        int j = 0;
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

class Threads // uso de threads para formar as combinações de primos e encontrar a maior possível
{
private:
    struct Instancias //estrutura que vai rodar e retornar o resultado de cada thread
    {
        std::thread funcao;
        std::vector<Pi_Primes> *max_pi;
        Instancias() { max_pi = nullptr; }
    };
    std::vector<Instancias> _threads;   // vetor (array) de threads que abro até MAX_THREADS
    std::vector<Pi_Primes> *threads_pi; // endereço do vetor com todos os primos de pi
    static size_t OPEN_THREADS;         // controle de threads abertas

public:
    Threads() { _threads.reserve(100); }
    ~Threads() { clear(); }

    size_t size() { return _threads.size(); } // tamanho da array de threads

    void join(const size_t &index) // acho mais prático fazer join, uma por uma,
    {                              // para poder já ir trabalhando os dados antes que todas tenham acabado
        if (index < _threads.size())
        {
            if (_threads[index].funcao.joinable())
            {
                _threads[index].funcao.join();
            }
            return;
        }
    }
    void join() // fecha todas as threads
    {
        for (auto &i : _threads)
        {
            if (i.funcao.joinable())
            {
                i.funcao.join();
            }
        }
    }
    void set(std::vector<Pi_Primes> *pi) { threads_pi = pi; } // definir endereço do veto de primos
    void clear()                                              // apagar o vetor para abrir mais threads
    {
        join();
        for (auto &i : _threads)
        {
            DELETE(i.max_pi);
        }
        _threads.clear();
        OPEN_THREADS = 0;
    }

    size_t add(void (*func)(std::vector<Pi_Primes> *, std::vector<Pi_Primes> **, int), int pos) // incluir uma thread
    {
        size_t index = _threads.size();

        if (OPEN_THREADS >= MAX_THREADS)
            return SIZE_MAX;

        _threads.resize(index + 1);
        OPEN_THREADS++;

        _threads[index].funcao = std::thread(func, threads_pi, &_threads[index].max_pi, pos);
        return index;
    }
    std::vector<Pi_Primes> *get(const size_t &index) { return _threads[index].max_pi; } // pegar o resultado da thread
};
size_t Threads::OPEN_THREADS = 0; // controle de threads abertas

void palavra(std::string &s, std::vector<Pi_Primes> *vector) // transforma a sequencia de primos em string para saber o tamanho da string
{
    s = "";
    if (vector == nullptr)
        return;
    for (auto &i : *vector)
    {
        s += i.number;
    }
}

void maior_seq(std::vector<Pi_Primes> *pi, std::vector<Pi_Primes> **max_pi, int pos) // forma as sequencias de primos
{
    std::vector<Pi_Primes> *resp, *tmp;
    std::string s_max, s_in;
    for (size_t i = pos + 1; i < pi->size(); i++)
    {
        if ((*pi)[pos].end == (*pi)[i].start)
        {
            resp = new std::vector<Pi_Primes>;
            maior_seq(pi, &resp, i);
            palavra(s_in, resp);
            if (*max_pi == nullptr || s_in.length() > s_max.length())
            {
                tmp = *max_pi;
                DELETE(tmp);
                *max_pi = resp;
                s_max = s_in;
            }
            else
                DELETE(resp);
        }
    }
    if (*max_pi == nullptr)
    {
        tmp = new std::vector<Pi_Primes>;
        *max_pi = tmp;
    }

    (*max_pi)->emplace((*max_pi)->begin(), (*pi)[pos]);
}

void merge(std::vector<Pi_Primes> &v1, const std::vector<Pi_Primes> &v2, int pos) // junta dois vetores a partir de uma posição do segundo
{
    for (pos = v2.size() - pos; pos < v2.size(); pos++)
        v1.push_back(v2[pos]);
}

int main()
{
    int pos = 0, progress = 0;
    char c = 0;
    char s1[2] = {0, 0}, s2[3] = {0, 0, 0}, s3[4] = {0, 0, 0, 0}, s4[5] = {0, 0, 0, 0, 0}; //usando char para dar mais velocidade, string é uma classe completa
    std::string s_in, s_max;
    std::vector<Pi_Primes> pi;
    std::vector<Pi_Primes> max_pi;
    std::vector<Pi_Primes> tmp;
    Primos primos;
    Threads threads;
    Pi_Primes entrar;

    std::cout << "uso: ./primospi < pi-1M.txt | aperte ctrl+C se não fez isso" << std::endl;

    while (std::cin >> c && c != '.') // pular o '3.'
        ;

    while (std::cin >> c) // após o . vai até não ter mais entradas
    {
        s1[0] = c;                                              // 1 numero
        s2[0] = s2[1], s2[1] = c;                               // 2 numeros
        s3[0] = s3[1], s3[1] = s3[2], s3[2] = c;                // 3 numeros
        s4[0] = s4[1], s4[1] = s4[2], s4[2] = s4[3], s4[3] = c; // 4 numeros

        if (primos.is_primo(s1))
        {
            entrar.set(pos, s1, pos + 1);
            pi.push_back(entrar);
        }

        if (s2[0] > 0 && primos.is_primo(s2)) //maior que 0 garante que o [0] está preenchido
        {
            entrar.set(pos - 1, s2, pos + 1);
            pi.push_back(entrar);
        }
        if (s3[0] > 0 && primos.is_primo(s3))
        {
            entrar.set(pos - 2, s3, pos + 1);
            pi.push_back(entrar);
        }
        if (s4[0] > 0 && primos.is_primo(s4))
        {
            entrar.set(pos - 3, s4, pos + 1);
            pi.push_back(entrar);
        }

        if (pi.size() > 0 && (pi.size() / ORGANIZE) > 1) // quando a variavel atinge 10mil entradas, reorganizar e deixar a maior entrada
        {
            std::sort(pi.begin(), pi.end()); //sort pelo índice de inicio.
            threads.set(&pi);
            threads.clear();
            for (size_t i = 0; i < pi.size() - 300; i++)
            {
                if (threads.add(maior_seq, i) == SIZE_MAX)
                {
                    i--;
                    for (size_t j = 0; j < threads.size(); j++)
                    {
                        threads.join(j);
                        if (threads.get(j) != nullptr)
                            palavra(s_in, threads.get(j));
                        if (threads.get(j) != nullptr && s_in.length() > s_max.length())
                        {
                            max_pi = *threads.get(j);
                            s_max = s_in;
                        }
                    }
                    threads.clear();
                }
            }
            for (size_t j = 0; j < threads.size(); j++)
            {
                threads.join(j);
                if (threads.get(j) != nullptr)
                    palavra(s_in, threads.get(j));
                if (threads.get(j) != nullptr && s_in.length() > s_max.length())
                {
                    max_pi = *threads.get(j);
                    s_max = s_in;
                }
            }
            threads.clear();
            tmp = max_pi;
            merge(max_pi, pi, 299);
            pi = max_pi;
            max_pi = tmp;
        }
        if ((pos / ORGANIZE) > progress) // esperar sem um aviso de trabalhando da ansiedade, a cada 10k numeros processados ele vai dizer
        {
            progress = pos / ORGANIZE;
            std::cout << progress << "0k..." << std::flush;
        }
        pos++;
    }
    std::cout << std::endl;
    std::sort(pi.begin(), pi.end());
    threads.set(&pi);
    threads.clear();
    for (size_t i = 0; i < pi.size() - max_pi.size(); i++)
    {

        if (threads.add(maior_seq, i) == SIZE_MAX)
        {
            i--;
            for (size_t j = 0; j < threads.size(); j++)
            {
                threads.join(j);
                if (threads.get(j) != nullptr)
                    palavra(s_in, threads.get(j));
                if (threads.get(j) != nullptr && s_in.length() > s_max.length())
                {
                    max_pi = *threads.get(j);
                    s_max = s_in;
                }
            }
            threads.clear();
        }
    }
    for (size_t j = 0; j < threads.size(); j++)
    {
        threads.join(j);
        if (threads.get(j) != nullptr)
            palavra(s_in, threads.get(j));
        if (threads.get(j) != nullptr && s_in.length() > s_max.length())
        {
            max_pi = *threads.get(j);
            s_max = s_in;
        }
    }
    threads.clear();

    for (auto &i : max_pi) // mostrar os numeros com espaço só pra confimar
        std::cout << i.number << " ";
    std::cout << std::endl;
    std::cout << s_max << std::endl; // mostrar o numero sem espaços

    return 0;
}
