#!/bin/bash

help() {
    echo -e "Anagramas em C++\n"
    echo -e "Comandos:"
    echo -e "  -build, -b\t\t- Compila o programa"
    echo -e "  -download, -d\t\t- Baixa o arquivo words.txt"
    echo -e "  -run, -r [palavra]\t- Executa o programa com a palavra fornecida ou 'barco' por padrão"
    echo -e "  -clean, -c\t\t- Exclui os arquivos gerados"
    echo -e "  -help, -h\t\t- Exibe as opções de comandos disponíveis\n"
    echo -e "Dependências:"
    echo -e "  - clang++ ou g++"
    echo -e "  - cmake"
    echo -e "  - curl"
    echo -e "  - make"
}

build() {
    cmake -S . -B build
    cmake --build build
}

download() {
    curl -O https://osprogramadores.com/desafios/d06/words.txt
}

run() {
    palavra=${1:-"barco"}
    
    if [ ! -f "words.txt" ]; then
        echo "Arquivo words.txt não encontrado!"
        echo "Por favor, execute './build.sh -download' para baixar."
    else
        ./build/Anagrama "$palavra" words.txt
    fi
}

clean() {
    rm -rf words.txt build
}

case "$1" in
    -help | -h)
        help
        ;;
    -build | -b)
        build
        ;;
    -download | -d)
        download
        ;;
    -run | -r)
        run "$2"
        ;;
    -clean | -c)
        clean
        ;;
    *)
        echo -e "Comando desconhecido.\nUse './build.sh -help' ou './build.sh -h para ver os comandos disponíveis."
        ;;
esac