import sqlite3

def conectar():
    return sqlite3.connect("SQLite (3).db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL,
        descricao TEXT,
        categoria TEXT,
        ativo INTEGER,
        imagem TEXT
    )""")
    conexao.commit()
    conexao.close()


def buscar_produtos():
   conexao = conectar()
   cursor = conexao.cursor()
   cursor.execute("SELECT * FROM Produtos WHERE ativo = 1")
   produtos = cursor.fetchall()
   
   listaDeProdutos= []

   for produto in produtos:
        produtoJson = {
            "id": produto[0],
            "nome": produto[1],
            "preco": produto[2],
            "descricao": produto[3],
            "categoria": produto[4],
            "imagem": produto[6]
        }
        listaDeProdutos.append(produtoJson)

        
   conexao.close()
   
   return listaDeProdutos


def criarProduto(nome,preco,descricao,categoria,imagem):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Produtos (nome, preco, descricao, categoria, imagem,ativo) VALUES (?, ?, ?, ?, ?,1)",
     (nome, preco, descricao, categoria, imagem)
    )
    conexao.commit()
    conexao.close()

def deletarProduto(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Produtos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    