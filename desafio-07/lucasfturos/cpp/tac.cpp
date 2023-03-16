#include <list>
#include <fstream>
#include <iostream>

auto main(int argc, char *argv[]) -> int {
    std::string buffer;
    std::ifstream file_txt(argv[1]);
    std::list<std::string> list_txt;

    if (!file_txt.is_open()) {
        std::cout << "Erro ao abrir o arquivo!!!" << '\n';
    }

    while (std::getline(file_txt, buffer, '\n')) {
        list_txt.push_front(buffer);
    }

    file_txt.close();

    for (auto i : list_txt) {
        std::cout << i << '\n';
    }
}
