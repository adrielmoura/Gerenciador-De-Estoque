# Gerenciador de Estoques (Python + SQLite)

 Um sistema simples de gerenciamento de estoque feito em Python, usando SQLite como banco de dados.
 Permite adicionar, remover, consultar e listar produtos em estoque.

 Funcionalidades

 Adicionar produto com quantidade inicial.

 Remover produto (com validação de quantidade).

 Consultar estoque de um produto específico.
 Listar todos os produtos cadastrados.

 Banco de dados local (estoque.db) usando SQLite.

 Tecnologias utilizadas

 Python 3

 SQLite3 (banco de dados embutido, não precisa instalar separado)

 Estrutura do projeto
 Gerenciador-De-Estoques/
   main.py           # Código principal do sistema
   estoque.db        # Banco de dados (criado automaticamente)
   README.md         # Documentação do projeto

 Como executar

 Clone o repositório (ou baixe os arquivos):

 git clone https://github.com/adrielmoura/gerenciador-de-estoques.git
 gerenciador-de-estoques


 Verifique se o Python está instalado:

 python3 --version


 Execute o programa:

 python3 main.py

 Exemplo de uso
 --- MENU ---
  1 - Adicionar produto
  2 - Remover produto
  3 - Listar produtos
  4 - Sair

  Se escolher 1, poderá adicionar um novo produto ao estoque.

  Se escolher 2, poderá remover certa quantidade de um produto existente.

  Se escolher 3, verá todos os produtos cadastrados.

  4 encerra o programa.