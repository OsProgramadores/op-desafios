run: build
	@if [ ! -f "words.txt" ]; then \
        echo "Arquivo words.txt não encontrado!\nPor favor, execute 'make download' para baixar."; \
    else \
        ./anagrama "barco" words.txt; \
    fi

build:
	@g++ -Wall -Wextra -Wpedantic -Werror -g -o anagrama main.cpp -std=c++2b

download:
	@if [ ! -f "words.txt" ]; then \
        echo "Baixando words.txt..."; \
        wget https://osprogramadores.com/desafios/d06/words.txt ; \
    else \
        echo "O arquivo já existe!"; \
    fi

clean:
	@rm -rf words.txt anagrama
