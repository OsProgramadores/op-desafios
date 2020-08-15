#include <cmath>
#include <iostream>

enum OPERACAO
{
    REGISTRA = 0,
    ESPACO = 1,
    ABRE = 2,
    FECHA = 3,
    POTENCIA = 4,
    MULTIPLICA = 8,
    DIVIDE = 16,
    SOMA = 32,
    SUBTRAI = 64
};

struct EXPRESSAO
{
    int numero;
    OPERACAO op;
    EXPRESSAO *abre;
    EXPRESSAO *anterior;
    EXPRESSAO *proxima;
    EXPRESSAO() : numero(0), op(REGISTRA), abre(nullptr), anterior(nullptr), proxima(nullptr) {}
    ~EXPRESSAO()
    { // limpeza de memória
        if (abre)
        {
            abre->anterior = nullptr;
            delete abre;
            abre = nullptr;
        }
        if (proxima)
        {
            proxima->anterior = nullptr;
            delete proxima;
            proxima = nullptr;
        }
        if (anterior)
        {
            delete anterior;
            anterior = nullptr;
        }
    }
};

class Expressao
{
private:
    EXPRESSAO *_exp_inicio;
    EXPRESSAO *atual;
    int parenteses;
    bool push(int numero, OPERACAO op)
    {
        if (atual == nullptr)
        {
            atual = new EXPRESSAO;
        }
        else
        {
            if (atual->op >= POTENCIA && op >= POTENCIA)
                return false;
            if (atual->op == ABRE && atual->abre == nullptr)
            {
                atual->abre = new EXPRESSAO;
                atual->abre->anterior = atual;
                atual = atual->abre;
            }
            else
            {
                atual->proxima = new EXPRESSAO;
                atual->proxima->anterior = atual;
                atual = atual->proxima;
            }
        }
        if (_exp_inicio == nullptr)
            _exp_inicio = atual;

        if (op == REGISTRA)
            atual->numero = numero;
        else
            atual->op = op;

        if (op == FECHA)
        {
            while (atual->abre == nullptr)
            {
                atual = atual->anterior;
                if (atual->abre != nullptr && atual->proxima != nullptr)
                    atual = atual->anterior;
            }
        }
        return true;
    }
    void resume(EXPRESSAO *inicio)
    {
        EXPRESSAO *tmp;
        int op_this[] = {POTENCIA, MULTIPLICA | DIVIDE, SOMA | SUBTRAI};
        while (inicio->op != ABRE && inicio->anterior != nullptr)
            inicio = inicio->anterior;

        for (auto &i : op_this)
        {
            atual = inicio;
            while (atual->proxima != nullptr || atual->abre != nullptr)
            {
                if ((int)atual->op & i)
                {
                    atual->anterior->numero = operacao(atual->anterior->numero, atual->proxima->numero, atual->op);
                    atual->anterior->proxima = atual->proxima->proxima;
                    if (atual->proxima->proxima != nullptr)
                        atual->proxima->proxima->anterior = atual->anterior;

                    apagar(atual->proxima);
                    tmp = atual->anterior;
                    apagar(atual);

                    atual = tmp;
                    if (atual->proxima == nullptr)
                        continue;
                }
                if (atual->op == ABRE)
                    atual = atual->abre;
                else
                    atual = atual->proxima;
            }
        }
    }
    int operacao(int a, int b, OPERACAO op)
    {
        if (a == INT32_MAX || b == INT32_MAX)
            return INT32_MAX;

        switch (op)
        {
        case POTENCIA:
            return pow(a, b);
        case MULTIPLICA:
            return a * b;
        case DIVIDE:
            if (b == 0)
                return INT32_MAX;
            return a / b;
        case SOMA:
            return a + b;
        case SUBTRAI:
            return a - b;
        default:
            return 0;
        }
    }
    void apagar(EXPRESSAO *no)
    {
        //isolar o nó para apagar sem sair
        //apagando toda a memória.
        no->abre = nullptr;
        no->anterior = nullptr;
        no->proxima = nullptr;
        delete no;
    }

public:
    Expressao() : _exp_inicio(nullptr), atual(nullptr), parenteses(0) {}
    ~Expressao() { clear(); }
    void clear()
    {
        parenteses = 0;
        atual = _exp_inicio;
        if (atual)
            delete atual;
        _exp_inicio = nullptr;
        atual = nullptr;
    }
    bool processar(const std::string &s)
    {
        int numero = 0, abre = 0;
        bool n_in = false;
        if (_exp_inicio != nullptr)
            clear();
        atual = nullptr;
        OPERACAO op = REGISTRA;
        for (auto &i : s)
        {
            switch (i)
            {
            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                numero = numero * 10 + (i - '0');
                n_in = true;
                break;
            case '^':
                op = POTENCIA;
                break;
            case '*':
                op = MULTIPLICA;
                break;
            case '/':
                op = DIVIDE;
                break;
            case '+':
                op = SOMA;
                break;
            case '-':
                op = SUBTRAI;
                break;
            case '(':
                op = ABRE;
                abre++;
                parenteses++;
                break;
            case ')':
                op = FECHA;
                abre--;
                if (abre < 0)
                    return false;
                break;
            case ' ':
                op = ESPACO;
                break;
            }
            if (op != REGISTRA)
            {
                if (n_in)
                {
                    if (!push(numero, REGISTRA))
                        return false;
                    n_in = false;
                }
                if (op != ESPACO && !push(0, op))
                    return false;

                numero = 0;
                op = REGISTRA;
            }
        }
        if (abre != 0)
            return false;
        if (n_in)
            push(numero, REGISTRA);
        return true;
    }
    int calcular()
    {
        atual = _exp_inicio;
        if (_exp_inicio == nullptr)
            return 0;
        while (parenteses > 0) // resolve os parenteses primeiro
        {
            atual = _exp_inicio;
            while (atual->op != FECHA)
            {
                if (atual->op == ABRE)
                    atual = atual->abre;
                else
                    atual = atual->proxima;
            }
            resume(atual);
            atual->anterior->anterior->op = REGISTRA;
            atual->anterior->anterior->numero = atual->anterior->numero;
            atual = atual->anterior->anterior;

            apagar(atual->abre->proxima);
            apagar(atual->abre);

            atual->abre = nullptr;
            parenteses--;
        }
        // todos os dados estão no mesmo nível, sem parenteses
        atual = _exp_inicio;
        resume(atual);
        return atual->numero;
    }
};

int main()
{
    std::string entrada;
    Expressao MyExp;
    int resp = 0;

    while (std::getline(std::cin, entrada))
    {
        if (!MyExp.processar(entrada))
        {
            std::cout << "ERR SYNTAX" << std::endl;
            continue;
        }
        if ((resp = MyExp.calcular()) == INT32_MAX)
        {
            std::cout << "ERR DIVBYZERO" << std::endl;
            continue;
        }
        std::cout << resp << std::endl;
    }
    return 0;
}
