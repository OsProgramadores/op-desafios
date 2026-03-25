run:
	@if [ ! -f "pi-1M.txt" ]; then \
        echo "Arquivo pi-1M.txt não encontrado. Por favor, execute 'make download' para baixar e descompactar o arquivo."; \
    else \
        python3 primos_pi.py pi-1M.txt; \
    fi
test:
	@if [ ! -f "pi-10000.txt" ]; then \
        echo "Arquivo pi-10000.txt não encontrado. Por favor, execute 'make cut-Pi-10000' para gerar o arquivo."; \
    else \
        python3 primos_pi.py pi-10000.txt; \
    fi
download:
	@if [ ! -f "pi-1M.tar.gz" ]; then \
        wget https://osprogramadores.com/files/d11/pi-1M.tar.gz && tar zxvf pi-1M.tar.gz; \
    else \
        echo "O arquivo já existe."; \
    fi
cut-Pi-10000:
	@cut -c1-10001 <pi-1M.txt >pi-10000.txt
clean:
	@rm -rf *.txt pi-1M.tar.gz
