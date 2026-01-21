from fastapi import FastAPI
from database import buscar_produtos
from database import criarProduto
from database import criar_tabela
from database import deletarProduto
from fastapi.middleware.cors import CORSMiddleware

# Create table if not exists
criar_tabela()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

@app.get('/produtos')
def listarProdutos():  
    produtos = buscar_produtos()
    
    return produtos

@app.post('/produtos')
def adicionar_produto(produto: dict):
    criarProduto(
        produto["nome"],
        produto["preco"],
        produto["descricao"],
        produto["categoria"],
        produto["imagem"]
    )
    return {"mensagem": "Produto criado"}

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    deletarProduto(id)
    return {"mensagem": "Produto deletado"}