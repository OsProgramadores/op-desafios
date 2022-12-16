#include <fstream>
#include <sstream>
#include <iostream>

std::string converteBase(uint64_t baseInput, uint64_t baseOutput, std::string numInput) {
    std::string bases{ "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" };
    std::string output;
    size_t numero{ 0 };
    size_t resto{ 0 };
    uint64_t aux{ 0 };
    if (baseInput > bases.length() || baseOutput > bases.length() || baseOutput < 2 || baseInput < 2) {
        return "???";
    }
    if (numInput == "0") {
        return numInput;
    }
    if (baseOutput < 62 && numInput == "???") {
        return "???";
    }
    output = "";
    while (!numInput.empty() && output != "???") {
        resto = 0;
        for (auto& i : numInput) {
            aux = bases.find(i);
            if (aux == std::string::npos || aux >= baseInput) {
                return "???";
            }
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

int main(int argc, char const* argv[]) {
    std::string numInput;
    std::string baseconv;
    uint64_t baseInput{ 0 };
    uint64_t baseOutput{ 0 };
    std::ifstream baseconvArq(argv[1]);

    if (!baseconvArq.is_open()) {
        std::cout << "Erro ao abrir o arquivo" << '\n';
        return 1;
    }

    while (std::getline(baseconvArq, baseconv)) {
        std::stringstream separaBases{ baseconv };
        while (separaBases >> baseInput >> baseOutput >> numInput) {
            std::cout << converteBase(baseInput, baseOutput, numInput) << '\n';
        }
    }
    baseconvArq.close();

    return 0;
}