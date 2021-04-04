# D5 - Python
- Esta implementação é uma otimização da implementação original do [Roger Demetrescu](https://github.com/rdemetrescu/OsProgramadores/blob/master/desafio-5/d05.py) para o Desafio 05 do site OsProgramadores.
- As otimizações implementadas consistem no seguinte:
    - A utilização da recente biblioteca `orjson` que parece ter um desempenho superior a da biblioteca nativa do python para as últimas versões testadas do python (3.6, 3.7 e 3.8)
    - A utilização de `f-strings` ao invés do antigo format de `str.format()`
    - Redução da criação de objetos, limpando as listas ao invés de criar novas

# Como Executar
- Deve-se ter na tua máquina uma versão do python 3 instalado e do gerenciador de pacotes do python: `pip`
- Instale as dependências rodando o comando `pip install -r requirements.txt`
- Rode o programa `python desafio5.py <path-to-file>`