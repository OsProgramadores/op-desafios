#include <algorithm>
#include <expected>
#include <fstream>
#include <iostream>
#include <string_view>
#include <unordered_map>
#include <unordered_set>
#include <variant>
#include <vector>

struct MaxLengthError {
    std::size_t length;
    std::string message = "Tamanho máximo da palavra/frase é de 16 caracteres!";
};

struct InvalidCharacterError {
    char invalidChar;
    std::string message = "Apenas caracteres de A-Z são válidos!";
};

struct FileOpenError {
    std::string fileName;
    std::string message;

    explicit FileOpenError(const std::string &name)
        : fileName(name), message("Não foi possível abrir o arquivo: " + name) {
    }
};

struct NoAnagramsError {
    std::string word;
    std::string message;

    explicit NoAnagramsError(const std::string &w)
        : word(w),
          message("Nenhum anagrama válido encontrado para a palavra/frase: " +
                  w) {}
};

using AnagramError = std::variant<MaxLengthError, InvalidCharacterError,
                                  FileOpenError, NoAnagramsError>;

class Anagrams {
  private:
    std::string m_InputWord;
    std::string m_Filename;
    std::unordered_set<std::string> m_ValidWords;
    std::unordered_set<std::string> m_ValidAnagrams;

    static std::unordered_map<char, int>
    computeCharFrequency(const std::string &word) {
        std::unordered_map<char, int> freq;
        for (char c : word) {
            freq[c]++;
        }
        return freq;
    }

    std::expected<void, AnagramError> processInputWord() {
        m_InputWord.erase(
            std::remove_if(m_InputWord.begin(), m_InputWord.end(), ::isspace),
            m_InputWord.end());

        if (m_InputWord.length() > 16) {
            return std::unexpected(MaxLengthError{m_InputWord.length()});
        }

        for (char &c : m_InputWord) {
            if (!static_cast<bool>(std::isalpha(c))) {
                return std::unexpected(InvalidCharacterError{c});
            }
        }

        std::transform(m_InputWord.begin(), m_InputWord.end(),
                       m_InputWord.begin(), ::toupper);

        return {};
    }

    std::expected<void, AnagramError> loadValidWords() {
        std::ifstream file(m_Filename);
        if (!file.is_open()) {
            return std::unexpected(FileOpenError{m_Filename});
        }

        std::string line;
        while (file >> line) {
            std::transform(line.begin(), line.end(), line.begin(), ::toupper);
            m_ValidWords.insert(line);
        }

        return {};
    }

    std::expected<void, AnagramError> generateValidAnagrams() {
        auto inputFreq = computeCharFrequency(m_InputWord);
        for (const auto &word : m_ValidWords) {
            if (word.length() == m_InputWord.length()) {
                auto wordFreq = computeCharFrequency(word);
                if (wordFreq == inputFreq && word != m_InputWord) {
                    m_ValidAnagrams.insert(word);
                }
            }
        }

        if (m_ValidAnagrams.empty()) {
            return std::unexpected(NoAnagramsError{m_InputWord});
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

  public:
    Anagrams(std::string_view inputWord, std::string_view filename)
        : m_InputWord(inputWord), m_Filename(filename) {}

    std::expected<void, AnagramError> run() {
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
        std::visit(
            [](const auto &error) {
                std::cerr << "Error: " << error.message << '\n';
            },
            result.error());
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
