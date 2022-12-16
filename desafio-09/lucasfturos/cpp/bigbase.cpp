#include <fstream>
#include <sstream>
#include <iostream>

class BigBase {
public:
    void manipulaArquivo(char const* argv);
    bool test(std::string numInput, std::uint32_t baseInput);
    std::string converteBase(std::uint32_t baseInput, std::uint32_t baseOutput, std::string numInput);
};

void BigBase::manipulaArquivo(char const* argv) {
    std::string numInput;
    std::string baseconv;
    std::uint32_t baseInput{ 0 };
    std::uint32_t baseOutput{ 0 };
    std::ifstream baseconvArq(argv);

    if (!baseconvArq.is_open()) {
        std::cout << "Erro ao abrir o arquivo" << '\n';
        std::exit(0);
    }

    while (std::getline(baseconvArq, baseconv)) {
        std::stringstream separaBases{ baseconv };
        while (separaBases >> baseInput >> baseOutput >> numInput) {
            std::cout << converteBase(baseInput, baseOutput, numInput) << '\n';
        }
    }
    baseconvArq.close();
}

std::string BigBase::converteBase(std::uint32_t baseInput, std::uint32_t baseOutput, std::string numInput) {
    std::string bases{ "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" };
    std::string output;
    size_t numero{ 0 };
    size_t resto{ 0 };
    std::uint32_t aux{ 0 };
    if (baseInput > bases.length() || baseOutput > bases.length() || baseOutput < 2 || baseInput < 2) {
        return "???";
    }
    if (numInput == "0") {
        return numInput;
    }
    if (baseOutput < 62 && test(numInput, baseInput)) {
        return "???";
    }
    output = "";
    while (numInput != "" && output != "???") {
        resto = 0;
        for (auto& i : numInput) {
            aux = bases.find(i);
            if (aux == std::string::npos || aux >= baseInput)
                return "???";
            numero = (resto * baseInput) + aux;
            resto = numero % baseOutput;
            i = bases[(numero / baseOutput)];
        }
        output = bases[resto] + output;
        while (numInput[0] == '0') {
            numInput = numInput.substr(1);
        }
    }
    if (baseOutput == 62) {
        if (output.length() > 30) {
            output = "???";
        }
    }
    return output;
}

bool BigBase::test(std::string numInput, std::uint32_t baseInput) {
    numInput = converteBase(baseInput, 62, numInput);
    if (numInput == "???") {
        return true;
    }
    return false;
}

int main(int argc, char const* argv[]) {
    BigBase bigbase;
    bigbase.manipulaArquivo(argv[1]);

    return 0;
}