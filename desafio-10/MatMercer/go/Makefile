.DEFAULT_GOAL := run

turing.tar.gz:
	@echo downloading turing programs...
	wget https://osprogramadores.com/files/d10/turing.tar.gz 2> /dev/null
	tar zxvf turing.tar.gz

turing: turing.tar.gz turing.go
	go build -o turing turing.go

.PHONY: run
run: turing
	@echo turing output:
	@echo
	@./turing datafile

.PHONY: run-debug
run-debug: export DEBUG = true
run-debug: turing
	@./turing datafile

clean:
	@echo "cleaning files"
	rm -f *.tur *.gz *.gz.* turing datafile


