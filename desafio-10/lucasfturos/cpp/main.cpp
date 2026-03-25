#include <algorithm>
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <unordered_map>
#include <vector>

struct Rules {
    std::string state;
    u_char symbol = '\0';
    u_char new_symbol = '\0';
    u_char direction = '\0';
    std::string new_state;
};

class TuringMachine {
  private:
    std::string m_rulefile;
    std::string state;

    std::vector<Rules> rules;
    std::unordered_map<std::string, std::size_t> rules_map;

    void loadRules() {
        std::string line;
        std::ifstream file(m_rulefile);
        if (!file.is_open()) {
            throw std::runtime_error("Erro ao abrir o arquivo!");
        }
        while (std::getline(file, line)) {
            if (line.empty()) {
                continue;
            }
            if (line[0] == ';') {
                continue;
            }
            Rules rule;
            std::istringstream line_stream(line);
            line_stream >> rule.state >> rule.symbol >> rule.new_symbol >>
                rule.direction >> rule.new_state;
            rules.push_back(rule);
        }
        file.close();

        std::sort(rules.begin(), rules.end(),
                  [](const Rules &a, const Rules &b) {
                      if (a.state != b.state) {
                          return a.state < b.state;
                      }
                      return a.symbol < b.symbol;
                  });

        std::string temp_state;
        for (std::size_t i = 0; i < rules.size(); ++i) {
            if (rules[i].state != temp_state) {
                temp_state = rules[i].state;
                rules_map[temp_state] = i;
            }
        }
    }

    std::size_t applyRules(u_char c) {
        std::size_t i = rules_map["*"];
        std::size_t wildcard_index = SIZE_MAX;
        if (c == ' ') {
            c = '_';
        }

        for (; i < rules.size() && rules[i].state == "*"; ++i) {
            if (rules[i].symbol == c) {
                wildcard_index = i;
                break;
            }
            if (rules[i].symbol == '*') {
                wildcard_index = i;
            }
        }

        i = rules_map[state];
        for (; i < rules.size() && rules[i].state == state; ++i) {
            if (rules[i].symbol == c) {
                return i;
            }
            if (rules[i].symbol == '*' && wildcard_index == SIZE_MAX) {
                wildcard_index = i;
            }
        }
        return wildcard_index;
    }

  public:
    explicit TuringMachine(const std::string &rulefile)
        : m_rulefile(rulefile), state("0") {
        loadRules();
    }

    void processRules(std::string &value) {
        if (value.empty()) {
            return;
        }
        state = "0";
        int i = 0;
        while (state.find("halt") == std::string::npos) {
            if (i < 0) {
                value = " " + value;
                i = 0;
            } else if (i == static_cast<int>(value.size())) {
                value += " ";
            }

            std::size_t rule_index = applyRules(value[i]);
            if (rule_index == SIZE_MAX) {
                value = "ERR";
                return;
            }

            if (rules[rule_index].new_state != "*") {
                state = rules[rule_index].new_state;
            }

            if (rules[rule_index].new_symbol == '_') {
                value[i] = ' ';
            } else if (rules[rule_index].new_symbol != '*') {
                value[i] = rules[rule_index].new_symbol;
            }

            if (rules[rule_index].direction == 'r') {
                i++;
            } else if (rules[rule_index].direction == 'l') {
                i--;
            } else if (rules[rule_index].direction != '*') {
                value = "ERR";
                return;
            }
        }
        value.erase(0, value.find_first_not_of(' '));
        value.erase(value.find_last_not_of(' ') + 1);
    }
};

int main(int argc, char **argv) {
    if (argc < 2) {
        std::cerr << "Uso: ./turing <nome_do_arquivo>" << '\n';
        return EXIT_FAILURE;
    }
    try {
        std::string filename = argv[1];
        std::ifstream file(filename);
        if (!file.is_open()) {
            throw std::runtime_error(
                std::string("Erro ao abrir o arquivo: " + filename));
        }

        std::string line;
        while (std::getline(file, line)) {
            std::istringstream line_stream(line);
            std::string rulefile;
            std::string value;
            if (std::getline(line_stream, rulefile, ',') &&
                std::getline(line_stream, value)) {
                auto tm = std::make_unique<TuringMachine>(rulefile);
                std::cout << rulefile << "," << value << ",";
                tm->processRules(value);
                std::cout << value << '\n';
            }
        }
    } catch (const std::exception &e) {
        std::cerr << e.what() << '\n';
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
