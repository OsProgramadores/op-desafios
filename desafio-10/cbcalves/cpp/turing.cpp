#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using std::cout;
using std::endl;
using std::fstream;
using std::getline;
using std::string;
using std::stringstream;
using std::swap;
using std::unordered_map;
using std::vector;

struct State
{
    string state;
    char symbol;
    char newsymbol;
    char direction;
    string newstate;

    State() : state(""), symbol(0), newsymbol(0), direction(0), newstate("") {}                             //iniciar as variáveis qdo criado
    void clear() { state = "", symbol = 0, newsymbol = 0, direction = 0, newstate = ""; }                   //limpar as variáveis
    int operator<(State B) { return state.compare(B.state.c_str()); }                                       //resposta ao sort, definição do operador <
    void operator<<(string s) { stringstream(s) >> state >> symbol >> newsymbol >> direction >> newstate; } //carregar as variáveis, mesmo se existir comentário ao lado ele ignora.
};

class Turing
{
private:
    unordered_map<string, size_t> _map; //map para lower_band
    vector<State> _turing;
    string rules_file, state;

    void quicksort(int l, int r) //sort do vetor (ou array) usará overload do operador < ao comparar as "regras", método de sort é quick sort
    {                            //existe método de sort mais rápido, porém numa array desse tamanho até bubble sort seria rápido
        vector<State>::iterator v = _turing.begin() + r;
        int i = l - 1, j = r;
        if (r <= l)
            return;
        while (1)
        {
            while (_turing[++i] < *v)
                ;
            while (*v < _turing[--j])
            {
                if (j == l)
                    break;
            }
            if (i >= j)
                break;
            swap(_turing[i], _turing[j]);
        }
        swap(_turing[i], _turing[r]);
        quicksort(l, i - 1);
        quicksort(i + 1, r);
    }

    void load() // carregar as regras
    {
        fstream fs;
        string line;
        State insert;
        fs.open(rules_file, fstream::in);
        if (!fs.is_open())
        {
            cout << "Arquivo de regras não encontrado" << endl;
            abort();
        }
        while (!fs.eof())
        {
            line = "";
            getline(fs, line);
            if (line[0] == ';' || line.length() == 0) // continua se for comentário ou linha vazia
                continue;
            insert.clear();
            insert << line;
            _turing.push_back(insert);
        }
        fs.close();
        quicksort(0, _turing.size() - 1); // sort nas regras
        line = "";
        for (size_t i = 0; i < _turing.size(); i++) // mapa de lower_band (mapear a primeira entrada de cada regra)
        {
            if (_turing[i].state != line)
            {
                line = _turing[i].state;
                _map[line] = i;
            }
        }
    }
    size_t rule(char c) // encontrar a regra desse símbolo para o atual estado
    {
        size_t i = _map["*"], isecond = SIZE_MAX; // lower_band do estado geral (se existir)
        if (c == ' ')                             // se for ' ' (espaço) tem que mudar para '_' que está nas regras
            c = '_';
        for (; i < _turing.size() && _turing[i].state == "*"; i++) //procura se tem no estado geral
        {
            if (_turing[i].symbol == c) // mais específica do estado geral
            {
                isecond = i;
                break;
            }
            if (_turing[i].symbol == '*') // menos específica do estado geral
                isecond = i;
        }
        i = _map[state];                                             // lower_band do estado
        for (; i < _turing.size() && _turing[i].state == state; i++) //procura se existe no estado atual
        {
            if (_turing[i].symbol == c) // achou a mais específica, retorna
                return i;
            if (_turing[i].symbol == '*' && isecond == SIZE_MAX) // menos específica no estado atual se a geral não existir(?)
                isecond = i;
        }
        return isecond; // retorna não achou (SIZE_MAX) ou achou uma menos específica
    }

public:
    Turing(const string &s) : rules_file(s), state("0") { load(); } // inicia as variáveis e lê o arquivo
    const string &get_filename() { return rules_file; } // retorna o nome do arquivo de regras
    void process(string &s) // processa a fita
    {
        size_t inrule = 0;
        int i = 0;

        if (s.length() == 0) // string vazia não existe o q fazer
            return;
        state = "0"; //estado "0" é sempre o início

        while (state.find("halt") == string::npos) //executar até existir halt
        {
            if (i == s.size()) //se leitor for maior q tamanho da string, aumenta a string
                s += " ";
            else if (i < 0) // se leitor for menor que o tamanho da string, aumenta a string
            {
                s = " " + s;
                i = 0;
            }
            inrule = rule(s[i]);    // achar a regra para a leitura no atual estado
            if (inrule == SIZE_MAX) // se não existe regra, algo de errado não está certo, abortar
            {
                s = "ERR";
                return;
            }
            state = (_turing[inrule].newstate == "*") ? state : _turing[inrule].newstate; //não acho que exista "*" mas vai que.

            if (_turing[inrule].newsymbol == '_') // se for '_' substitui por espaço
                s[i] = ' ';
            else if (_turing[inrule].newsymbol != '*') // se não for '*' substitui a letra, se for '*' não faz nada
                s[i] = _turing[inrule].newsymbol;

            if (_turing[inrule].direction == 'r') // move o leitor para a direita
                i++;
            else if (_turing[inrule].direction == 'l') // move o leitor para a esquerda,
                i--;
            else if (_turing[inrule].direction != '*') // se for '*' não faz nada, se for diferente aborta o programa
            {
                s = "ERR";
                return;
            }
        }
        for (i = 0; i < s.size(); i++) // left trim (apagar os espaço à esquerda da fita em branco)
        {
            if (s[i] == ' ')
                s = s.substr(i + 1), i--;
            else
                break;
        }
        for (i = s.size() - 1; i >= 0; i--) // right trim (apagar os espaços à direita da fita em branco)
        {
            if (s[i] == ' ')
                s = s.substr(0, i);
            else
                break;
        }
        return;
    }
};

int main(int argv, char *argc[])
{
    fstream df;
    string filename, command;
    Turing *mytur = nullptr;
    if (argv < 2)
        return 0;
    filename = argc[1];
    if (filename.find(',') == string::npos) // se não achar virgula ele lê o arquivo com várias regras
    {
        df.open(filename, fstream::in);
        if (!df.is_open())
        {
            cout << "Arquivo não encontrado" << endl;
            abort();
        }
        while (!df.eof())
        {
            filename = "";
            getline(df, filename);
            if (filename.length() == 0) // continua se for vazia
                continue;
            command = filename.substr(filename.find(',') + 1);
            filename = filename.substr(0, filename.find(','));

            if (mytur != nullptr && mytur->get_filename() != filename) // se a regra for a mesma não precisa recarregar
            {
                delete mytur;
                mytur = nullptr;
            }
            if (mytur == nullptr)
                mytur = new Turing(filename); // carrega as regras

            cout << filename << "," << command << ",";
            mytur->process(command); // processa a fita
            cout << command << endl; // posta o resultado da fita
        }
        df.close();
    }
    else // se achar virgula ele entende q é um arquivo com regra (serviu pros testes iniciais)
    {
        command = filename.substr(filename.find(',') + 1);
        filename = filename.substr(0, filename.find(','));
        mytur = new Turing(filename); // carrega as regras
        cout << filename << "," << command << ",";
        mytur->process(command); // processa a fita
        cout << command << endl; // posta o resultado da fita
        delete mytur;
    }
    return 0;
}
