run: build
	@if [ ! -f "datafile" ]; then \
        echo "Arquivo datafile não encontrado. Por favor, execute 'make download' para baixar e descompactar o arquivo."; \
    else \
        ./turing datafile; \
    fi
build:
	@g++ -Wall -Wextra -Wpedantic -Werror -pedantic -g -o turing main.cpp
download:
	@if [ ! -f "turing.tar.gz" ]; then \
        wget https://osprogramadores.com/files/d10/turing.tar.gz && tar zxvf turing.tar.gz; \
    else \
        echo "O arquivo já existe."; \
    fi
clean:
	@rm -rf turing datafile *.tur *.tar.* *.txt
