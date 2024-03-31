# Introdução

Implementação do comando _tac_ que lê um arquivo e exibe as linhas em ordem inversa - da última para a primeira


# Verificação do código com Pylint

O comando a seguir altera o diretório para a pasta do desafio:

```shell
cd desafio-07/disouzam/python
```

Executando dentro da pasta do desafio (desafio-07/disouzam/python), o comando para verificar o código através do Pylint é:

```python
pylint --rcfile=../../../ci/pylint3.rc tac.py
```

# Descompactação do arquivo de teste

```shell
gzip -d 1GB.txt.gz
```

Verificação da integridade do arquivo usando o tac
```shell
tac 1GB.txt | md5sum
```

Resultado: 
```
2b4fd25f11d75c285ec69ecac420bd07
```

# Como executar o script

Esse código foi testado com a versão 3.12.1 do Python e pode apresentar alguma instabilidade com o Python 3.11 (não foi checado contra essa versão).

Executando dentro da pasta do desafio (desafio-07/disouzam/python), o comando para ler e processar o arquivo de teste é:

```python
python -m tac 1GB.txt
```

Teste e conferência dos resultados:
```shell
python -m tac 1GB.txt | md5sum
```

Resultado esperado:
```shell
2b4fd25f11d75c285ec69ecac420bd07
```

Usando um arquivo mais simples, extraído da página de instruções do desafio ([#7: UNIX TAC](https://osprogramadores.com/desafios/d07/)) para fins de desenvolvimento, o comando é:

```python
python -m tac exemplo1.txt
```

# Verificação em estágios

Conforme explicado no commit **9597e92** - O conteúdo revertido é escrito também num arquivo temporário para verificação, alguma razão não esclarecida faz que o md5sum obtido usando pipes no shell (f742e75495168191e16793cd3eea2902) não coincida com o md5sum esperado (2b4fd25f11d75c285ec69ecac420bd07). Suspeita-se que tenha a ver com o caracter de final de linha ou algo específico do sistema Windows. Várias tentativas foram feitas e muitas buscas na internet para tentar resolver o problema mas não consegui uma boa solução até o momento.

A solução que eu apresento é retornar o conteúdo revertido usando o mecanismo do tac original em um arquivo temporário (_temp_file.txt_) e verificar o md5sum usando o cat nesse arquivo. Veja abaixo exemplos da simulação e uma imagem será inserida no pull request

```shell
python -m tac 1GB.txt | md5sum
f742e75495168191e16793cd3eea2902

cat temp_file.txt | md5sum
2b4fd25f11d75c285ec69ecac420bd07

tac 1GB.txt | md5sum
2b4fd25f11d75c285ec69ecac420bd07
```
