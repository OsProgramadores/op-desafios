// compile:
//g++ main.cpp -o foo

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

typedef std::vector<std::string> Dict;

void printDict(const Dict &dict)
{
    for (auto i = 0; i < dict.size(); i++)
    {
        std::cout << dict[i];

        if (i < dict.size() - 1)
        {
            std::cout << " ";
        }
    }

    std::cout << std::endl;
}

std::string validInputAndToUpper(const char *input)
{
    std::string inputStr(input);

    inputStr.erase(std::remove(inputStr.begin(), inputStr.end(), ' '), inputStr.end());

    if (inputStr.length() > 16)
    {
        throw std::runtime_error("Tamanho maximo da palavra são 16 caracteres");
    }
    for (char c : inputStr)
    {
        if (!std::isalpha(c))
        {
            throw std::runtime_error("São validos apenas carateres de A-Z");
        }
    }
    std::transform(inputStr.begin(), inputStr.end(), inputStr.begin(), ::toupper);
    return inputStr;
}

Dict loadDict(const char *dictFile)
{
    Dict dict;
    std::string word;
    std::ifstream file(dictFile);

    try
    {
        if (!file.is_open())
        {
            throw std::runtime_error("Falha ao abrir o arquivo!");
        }

        while (std::getline(file, word))
        {
            dict.push_back(word);
        }
    }
    catch (const std::exception &e)
    {
        throw std::runtime_error(e.what());
    }

    file.close();

    return dict;
}

Dict removeWrongWords(const std::string userWord, const Dict &dict)
{
    Dict newDict;

    for (auto &word : dict)
    {
        std::string newUserWord = userWord;
        bool isBreak = false;
        for (auto &letter : word)
        {
            if (newUserWord.find(letter) != std::string::npos)
            {
                newUserWord.erase(newUserWord.find(letter), 1);
            }
            else
            {
                isBreak = true;
                break;
            }
        }
        if (!isBreak)
        {
            newDict.push_back(word);
        }
    }

    return newDict;
}

Dict buildAnagrams(const std::string userWord, Dict &dict, Dict &anagram)
{
    auto word = std::string(dict[0]);
    dict.erase(dict.begin());

    Dict newAnagram = Dict(anagram);
    newAnagram.push_back(word);

    auto newUserWord = userWord;

    for (auto letter : word)
    {
        newUserWord.erase(newUserWord.find(letter), 1);
    }

    auto newDict = removeWrongWords(newUserWord, dict);

    if (newUserWord.size() == 0)
    {
        return newAnagram;
    }
    else
    {
        auto sizeListWords = newDict.size();

        for (auto i = 0; i < sizeListWords; i++)
        {
            auto isAnagram = buildAnagrams(newUserWord, newDict, newAnagram);
            if (isAnagram.size() > 0)
            {
                printDict(isAnagram);
            }
        }
    }
    return {};
}

void solvesAnagram(const std::string userWord, Dict &dict)
{
    dict = removeWrongWords(userWord, dict);
    auto sizeDict = dict.size();

    for (auto i = 0; i < sizeDict; i++)
    {
        Dict anagram;
        buildAnagrams(userWord, dict, anagram);
    }
}

int main(int argc, char const *argv[])
{
    if (argc < 3)
    {
        std::cerr << "Use:\n ./foo palavra words.txt\n";
        return 2;
    }

    std::string userWord;
    Dict dict;

    try
    {
        userWord = validInputAndToUpper(argv[1]);
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
        return 2;
    }

    try
    {
        dict = loadDict(argv[2]);
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
        return 1;
    }

    solvesAnagram(userWord, dict);

    return 0;
}