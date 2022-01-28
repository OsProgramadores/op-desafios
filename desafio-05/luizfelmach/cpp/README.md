# Como rodar este código

- **Baixe** a dependência de parser do JSON no **mesmo path** que o arquivo que será compilado com o nome `json.hpp`. Rode o comando abaixo:
```properties
curl -o json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp
```

- Utilize o g++ para compilar o código. Foi testado na versão: g++ (GCC) 11.2.1 20210728 (Red Hat 11.2.1-1).
- Para compilar e rodar o código, rode os comandos abaixo:

```properties
g++ -o desafio5 desafio5.cpp
./desafio5 <path-to-json>
```
