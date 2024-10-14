#include <algorithm>
#include <fstream>
#include <iostream>
#include <memory>
#include <unordered_set>
#include <vector>

class Anagrams {
  private:
    std::string m_InputWord;
    std::unordered_set<std::string> m_ValidWords;
    std::unordered_set<std::string> m_ValidAnagrams;

  public:
    Anagrams(const std::string &inputWord, const std::string &filename)
        : m_InputWord(inputWord) {
        processInputWord();
        loadValidWords(filename);
        generateValidAnagrams();
    }

    void processInputWord() {
        m_InputWord.erase(
            std::remove_if(m_InputWord.begin(), m_InputWord.end(), ::isspace),
            m_InputWord.end());

        if (m_InputWord.length() > 16) {
            throw std::runtime_error(
                "Tamanho máximo da palavra/frase é de 16 caracteres!");
        }

        std::for_each(m_InputWord.begin(), m_InputWord.end(), [](char &c) {
            if (!static_cast<bool>(std::isalpha(c))) {
                throw std::runtime_error(
                    "Apenas caracteres de A-Z são válidos!");
            }
        });

        std::transform(m_InputWord.begin(), m_InputWord.end(),
                       m_InputWord.begin(), ::toupper);
    }

    void loadValidWords(const std::string &filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            throw std::runtime_error("Não foi possível abrir o arquivo: " +
                                     filename);
        }

        std::string line;
        while (file >> line) {
            std::transform(line.begin(), line.end(), line.begin(), ::toupper);
            m_ValidWords.insert(line);
        }
    }

    void generateValidAnagrams() {
        std::string tempWord = m_InputWord;
        std::sort(tempWord.begin(), tempWord.end());

        do {
            if (tempWord != m_InputWord &&
                m_ValidWords.find(tempWord) != m_ValidWords.end()) {
                m_ValidAnagrams.insert(tempWord);
            }
        } while (std::next_permutation(tempWord.begin(), tempWord.end()));

        if (m_ValidAnagrams.empty()) {
            throw std::runtime_error(
                "Nenhum anagrama válido encontrado para a palavra: " +
                m_InputWord);
        }
    }

    void print() {
        std::vector<std::string> sortedAnagrams(m_ValidAnagrams.begin(),
                                                m_ValidAnagrams.end());
        std::sort(sortedAnagrams.begin(), sortedAnagrams.end());
        std::for_each(
            sortedAnagrams.begin(), sortedAnagrams.end(),
            [](const std::string &anagram) { std::cout << anagram << '\n'; });
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

    std::string inputWord = argv[1];
    std::string filename = argv[2];

    try {
        auto anagram = std::make_shared<Anagrams>(inputWord, filename);
        anagram->print();
    } catch (const std::exception &e) {
        std::cerr << "Erro: " << e.what() << '\n';
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
