#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <climits>

/**
 * Operações matemáticas suportadas
 * EXPONENCIAR, MULTIPLICAR, DIVIDIR, SOMAR e SUBTRAIR
 */
enum OPERACAO {
    REGISTRAR   = 0,
    EXPONENCIAR = 1 << 0,
    MULTIPLICAR = 1 << 1,
    DIVIDIR     = 1 << 2,
    SOMAR       = 1 << 3,
    SUBTRAIR    = 1 << 4
};

/**
 * Estrutura para gardar o numero e a operação associada
 */
struct expressao_t {
    int numero;
    OPERACAO operacao;
    inline expressao_t(int n, OPERACAO op) : numero(n), operacao(op) {}
};

/**
 * Classe para resolver a expressão
 */
class Expressao
{
private:
    std::vector<expressao_t> _expressao;
    int _pos;

    /**
     * Auxiliar para preenchimento do vetor
     */
    inline void push(int numero, OPERACAO op)
    {
        _expressao.push_back(expressao_t(numero, op));
    }

    /**
     * Realiza a operação matemática
     */
    int operacao(int a, int b, OPERACAO op)
    {
        if (a == INT_MAX || b == INT_MAX) {
            return INT_MAX;
        }

        switch (op) {
        case EXPONENCIAR: return pow(a, b);
        case MULTIPLICAR: return a * b;
        case SOMAR:       return a + b;
        case SUBTRAIR:    return a - b;
        case DIVIDIR:
            if (b == 0) {
                return INT_MAX;
            }
            return a / b;

        default: return 0;
        }
    }

    /**
     * Auxiliar para retorno de posição ao resolver expressões
     * paralelas entre parenteses
     */
    inline int getPos()
    {
        return _pos;
    }

    /**
     * Processar a string contendo a expressão matemática
     * decompondo em um vetor de operações
     */
    bool processar(const std::string &str, bool state)
    {
        Expressao temp;
        int numero = 0;
        bool args = true;

        for (int i = 0; i < (int)str.size(); i++) {
            switch (str[i]) {
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
                numero = numero * 10 + (str[i] - '0');
                args = false;
                break;
            case '^':
                push(numero, EXPONENCIAR);
                goto commonPoint;
            case '*':
                push(numero, MULTIPLICAR);
                goto commonPoint;
            case '/':
                push(numero, DIVIDIR);
                goto commonPoint;
            case '+':
                push(numero, SOMAR);
                goto commonPoint;
            case '-':
                push(numero, SUBTRAIR);

            commonPoint:
                if (args) {
                    return false;
                }
                numero = 0;
                args = true;
                break;
            case '(':
                if (!args) {
                    return false;
                }

                // Em caso de abertura de parentese, cria uma nova
                // instância e processando o parentese.
                temp.clear();
                if (temp.processar(str.substr(i + 1), false)) {
                    return false;
                }
                numero = temp.calcular();
                args = false;
                i += temp.getPos();
                break;
            case ')':
                push(numero, REGISTRAR);
                _pos = i + 1;
                return false;
            }
        }
        push(numero, REGISTRAR);

        return state;
    }

public:
    Expressao() : _pos(0){};

    /**
     * Limpar todas as variáveis da classe
     */
    void clear()
    {
        _expressao.clear();
        _pos = 0;
    }

    /**
     * Processar a string contendo a expressão matemática
     * decompondo em um vetor de operações
     */
    bool processar(const std::string &str)
    {
        return processar(str, true);
    }

    /**
     * Calcula o vetor gerado pela decomposição da string
     */
    int calcular()
    {
        int op_precedencia[] = {EXPONENCIAR, MULTIPLICAR | DIVIDIR, SOMAR | SUBTRAIR};
        for (auto &op : op_precedencia) {
            for (auto i = _expressao.begin(); i < _expressao.end() - 1; i++) {
                while ((i->operacao & op) > 0) {
                    i->numero = operacao(i->numero, (i + 1)->numero, i->operacao);
                    i->operacao = (i + 1)->operacao;
                    if (i->numero == INT_MAX) {
                        return INT_MAX;
                    }
                    _expressao.erase(i + 1);
                }
            }
        }
        return _expressao[0].numero;
    }
};

int main()
{
    std::string entrada;
    Expressao myExpression;

    // Remover os espaços da string
    auto removeSpace = [](std::string &str) {
        for (auto i = str.begin(); i < str.end(); i++) {
            if (*i == ' ') {
                str.erase(i);
            }
        }
    };

    while (std::getline(std::cin, entrada)) {
        myExpression.clear();
        removeSpace(entrada);

        if (!myExpression.processar(entrada)) {
            std::cout << "ERR SYNTAX" << std::endl;
            continue;
        }

        int resp;
        if ((resp = myExpression.calcular()) == INT_MAX) {
            std::cout << "ERR DIVBYZERO" << std::endl;
            continue;
        }
        std::cout << resp << std::endl;
    }
    return 0;
}
