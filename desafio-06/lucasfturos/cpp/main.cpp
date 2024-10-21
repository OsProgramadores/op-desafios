#include <algorithm>
#include <expected>
#include <fstream>
#include <iostream>
#include <string_view>
#include <unordered_set>
#include <vector>

class Anagrams {
  private:
    std::string m_InputWord;
    std::string m_Filename;
    std::unordered_set<std::string> m_ValidWords;
    std::unordered_set<std::string> m_ValidAnagrams;

    using ExpectedResult = std::expected<void, std::string>;

  public:
    Anagrams(std::string_view inputWord, std::string_view filename)
        : m_InputWord(inputWord), m_Filename(filename) {}

    ExpectedResult processInputWord() {
        m_InputWord.erase(
            std::remove_if(m_InputWord.begin(), m_InputWord.end(), ::isspace),
            m_InputWord.end());

        if (m_InputWord.length() > 16) {
            return std::unexpected(
                "Tamanho máximo da palavra/frase é de 16 caracteres!");
        }

        for (char &c : m_InputWord) {
            if (!static_cast<bool>(std::isalpha(c))) {
                return std::unexpected("Apenas caracteres de A-Z são válidos!");
            }
        }

        std::transform(m_InputWord.begin(), m_InputWord.end(),
                       m_InputWord.begin(), ::toupper);

        return {};
    }

    ExpectedResult loadValidWords() {
        std::ifstream file(m_Filename);
        if (!file.is_open()) {
            return std::unexpected("Não foi possível abrir o arquivo: " +
                                   m_Filename);
        }

        std::string line;
        while (file >> line) {
            std::transform(line.begin(), line.end(), line.begin(), ::toupper);
            m_ValidWords.insert(line);
        }

        return {};
    }

    ExpectedResult generateValidAnagrams() {
        std::string tempWord = m_InputWord;
        std::sort(tempWord.begin(), tempWord.end());

        do {
            if (tempWord != m_InputWord &&
                m_ValidWords.find(tempWord) != m_ValidWords.end()) {
                m_ValidAnagrams.insert(tempWord);
            }
        } while (std::next_permutation(tempWord.begin(), tempWord.end()));

        if (m_ValidAnagrams.empty()) {
            return std::unexpected(
                "Nenhum anagrama válido encontrado para a palavra: " +
                m_InputWord);
        }

        return {};
    }

    void printAnagrams() const {
        std::vector<std::string> sortedAnagrams(m_ValidAnagrams.begin(),
                                                m_ValidAnagrams.end());
        std::sort(sortedAnagrams.begin(), sortedAnagrams.end());
        for (const auto &anagram : sortedAnagrams) {
            std::cout << anagram << '\n';
        }
    }

    ExpectedResult run() {
        if (auto result = processInputWord(); !result) {
            return std::unexpected(result.error());
        }

        if (auto result = loadValidWords(); !result) {
            return std::unexpected(result.error());
        }

        if (auto result = generateValidAnagrams(); !result) {
            return std::unexpected(result.error());
        }

        printAnagrams();

        return {};
    }
};

int main(int argc, char **argv) {
    if (argc < 3) {
        std::cerr << "Informe uma palavra/frase (limite de 16 caracteres) para "
                     "gerar anagramas e o arquivo de palavras (words.txt)!\n";
        std::cerr << "Exemplo de uso: ./anagrama " << '"' << "<frase/palavra>"
                  << '"' << " words.txt\n";
        return EXIT_FAILURE;
    }

    std::string_view inputWord = argv[1];
    std::string_view filename = argv[2];

    Anagrams anagram(inputWord, filename);
    if (auto result = anagram.run(); !result) {
        std::cerr << "Erro: " << result.error() << '\n';
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
