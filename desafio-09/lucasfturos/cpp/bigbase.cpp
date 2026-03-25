#include <fstream>
#include <iostream>
#include <sstream>

std::string converteBase(uint64_t baseInput, uint64_t baseOutput, std::string numInput) {
    uint64_t aux{ 0 };
    std::string output;
    size_t num{ 0 }, rest{ 0 };
    std::string bases{ "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" };

    if (numInput == "0") {
        return numInput;
    }

    if (baseOutput < 62 && numInput == "???") {
        return "???";
    }

    if (baseInput > bases.length() || baseOutput > bases.length() ||
        baseOutput < 2 || baseInput < 2) {
        return "???";
    }

    output = "";
    while (!numInput.empty() && output != "???") {
        rest = 0;

        for (auto& i : numInput) {
            aux = bases.find(i);
            if (aux == -1UL || aux >= baseInput) {
                return "???";
            }
            num = (rest * baseInput) + aux;
            rest = num % baseOutput;
            i = bases[(num / baseOutput)];
        }

        output = bases[rest] + output;

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
    std::string numInput, baseconv;
    uint64_t baseInput{ 0 }, baseOutput{ 0 };
    std::ifstream baseconvArq(argv[1]);

    if (!baseconvArq.is_open()) {
        std::cout << "Erro ao abrir o arquivo" << '\n';
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
