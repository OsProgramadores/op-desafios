run: build
	@ulimit -v 524288 && ./tac 1GB.txt | md5sum
build:
	@g++ -Wall -o tac tac.cpp
download:
	wget https://osprogramadores.com/files/d07/1GB.txt.gz
	gzip -d 1GB.txt.gz
remove:
	@rm -rf 1GB.txt.gz 1GB.txt tac
