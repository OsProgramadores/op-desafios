#include <fstream>
#include <iostream>

auto reverseStr(std::string invert_order) -> std::string {
    std::uint64_t size{invert_order.length()};
    for (auto i{0UL}; i < size / 2; ++i) {
        std::swap(invert_order[i], invert_order[size - i - 1]);
    }
    return invert_order;
}

auto main(int argc, char *argv[]) -> int {
    std::string buffer;
    std::string buffer_str;
    std::streampos pos{};
    std::ifstream file_txt(argv[1]);

    if (!file_txt.is_open()) {
        std::cout << "Erro ao abrir o arquivo!!!" << '\n';
    }

    file_txt.seekg(-1, std::ios::end);
    pos = file_txt.tellg() + 1L;

    while (pos) {
        buffer_str = file_txt.get();
        if (buffer_str == "\n" || pos == 1L) {
            if (pos == 1L) {
                buffer += buffer_str;
            }
            std::cout << reverseStr(buffer);
            buffer.clear();
        }
        buffer += buffer_str;
        file_txt.seekg(-2, std::ios::cur);
        pos -= 1L;
    }

    file_txt.close();
}
