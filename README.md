# op-desafios

Este repositório contém as soluções para os desafios em http://osprogramadores.com/desafios.

# Como contribuir

1. Faça um fork deste repositório clicando no botão `Fork` no canto superior da tela.
1. Faça um clone do repositório para a sua estação de trabalho:
   ```
   $ git clone https://github.com/<seu_usuario>/op-desafios
   ```
1. Entre no diretorio criado pelo git (`op-desafios`).

1. Crie um remote apontando para o repositório dos OsProgramadores:

   ```
   $ git remote add upstream https://github.com/OsProgramadores/op-desafios
   ```

1. Uma vez feito o fork, crie um branch de trabalho (por exemplo, "dev")

   ```
   $ git checkout -b dev
   ```

1. Trabalhe normalmente no branch de desenvolvimento. Quando estiver satisfeito com o resultado, faça o commit e o push com:

   ```
   $ git push origin dev
   ```

1. O branch usado no "git checkout" tem que casar com o branch usado no "git push".

1. Entre no github e abra um Pull Request (PR).

1. Fique atento a erros na página do Pull Request (indicando que os testes de integração falharam) ou comentários dos admins. Se alterações forem necessárias, modifique o fonte e faça outro "git commit" seguido de "git push origin dev". Não é necessário fechar o PR e abrir outro.

# Estrutura de diretórios

Ao criar um novo programa, mantenha a estrutura abaixo:

```
desafio-01/
  seu_usuario_no_github/
    linguagem-feature/
      arquivos com a sua solução
      README.md <-- comentários, opcional.
    ...
desafio-02/
  seu_usuario_no_github/
    linguagem-feature/
      arquivos com a sua solução
    ...
```

* **Linguagem** é a linguagem em que o seu programa foi feito (em minúsculas). Olhe os outros casos de nomes de linguagens usadas no repo e mantenha o padrão.

* **feature** é um diferenciador de uma _feature_ dentro da linguagem. Por exemplo, dois programas em python usando duas libraries, uma chamada _foo_ e uma chamada _bar_, ficariam em dois diretorios separados: `python-libfoo` e `python-libbar`. Só submeta mais de uma versão por linguagem se a diferença no programa for significativa.

* Arquivos com espaços ou caracteres não ASCII (acentos, emoji, etc) não serão aceitos no repositório.

# Observações para linguagens específicas

## Python

1. Apenas python3 é suportado.

1. Use **espaços** (não tabs!) para indentar o seu código.

1. Use indentação em **4 espaços**.

1. Cheque o seu código com o [pylint](http://pylint.org) antes de enviar. O arquivo de configuração usado pelo depo está em `travis-ci/pylint3.rc`. Para checar o seu programa, rode:

   ```
   $ pylint --rcfile=<diretorio_do_seu_repo>/travis-ci/pylint3.rc <nome_do_seu_arquivo.py>
   ```

1. Pull Requests contendo código em Python serão automaticamente verificados pelo pylint. Ao submeter um PR, observe a tela do PR e verifique se a integração falhou. Em caso de erro, clique no link e verifique as mensagens de erro do pylint. Corrija o código, faça outro submit e push.

Em caso de problemas ou dúvidas, entre em contato com um dos administradores.
