import sqlite3

class Gestao:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()
    
    def criar_tabela_estoque(self):
        curso = self.conn.cursor()
        curso.execute('''CREATE TABLE IF NOT EXISTS estoque (
                         id INTEGER PRIMARY KEY, 
                         produto TEXT, 
                         quantidade INTEGER)''')
        self.conn.commit()

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, quantidade) VALUES (?,?)", (produto, quantidade))
        self.conn.commit()

    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
                cursor.execute("UPDATE estoque SET quantidade=? WHERE produto=?",
                               (estoque_atual - quantidade, produto))
                self.conn.commit()
            else:
                print(f"Quantidade insuficiente do {produto} em estoque.")
        else:
            print(f"{produto} não encontrado em estoque.")

    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0
        
    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto, quantidade FROM estoque")
        produtos = cursor.fetchall()
        return [(produto, quantidade) for produto, quantidade in produtos]

sistema = Gestao("estoque.db")

while True:
    print("\n---MENU---")
    print("1- Adicionar produto")
    print("2- Remover produto")
    print("3- Listar produtos")
    print("4- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            produto = input("Nome do produto (ou 'sair para voltar ao menu'): ")
            if produto.lower() == "sair":
                break
            quantidade = int(input("Quantidade do produto: "))
            sistema.adicionar_produto(produto, quantidade)
            print(f"{produto} adicionado com {quantidade} unidades.")
    
    elif opcao == "2":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade a remover: "))
        sistema.remover_produto(produto, quantidade)
        
    elif opcao == "3":
       produtos_em_estoque = sistema.listar_produtos()
       for produto, quantidade in produtos_em_estoque:
        print(f"Produto: {produto} | Quantidade: {quantidade}")

    elif opcao == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")