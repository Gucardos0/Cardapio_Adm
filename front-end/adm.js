
function fazPost(url, body){
        fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(body)
})
.then(resposta => resposta.json())
.then(data =>{
    console.log("Resposta da API:", data)
    alert("Produto criado!")
})
  .catch(err => console.error("Erro:", err))
}

const adicionarProduto = ()=>{
    event.preventDefault()
    let url = 'http://127.0.0.1:8000/produtos'
    let nome= document.getElementById("nome_novoP").value
    let preco= document.getElementById("preco_novoP").value
    let descricao= document.getElementById("descricao_novoP").value
    let categoria= document.getElementById("categoria_novoP").value
    let imagem= document.getElementById("imagem_novoP").value

    let body ={
        'nome': nome,
        'preco':preco,
        'descricao':descricao,
        'categoria':categoria,
        'imagem':imagem

    }

    console.log(body)
    
    fazPost(url, body)
    
}

const deletarProduto = (event) => {
    event.preventDefault()

    let id = document.getElementById("item_id").value

    if(!id){
        alert("Digite o ID do produto")
        return
    }

    fetch(`http://127.0.0.1:8000/produtos/${id}`, {
        method: "DELETE"
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)
        alert("Produto deletado!")
    })
    .catch(err => console.error("Erro:", err))
}

 


    


    
const BtnAdd = document.getElementById("Adicionar")
BtnAdd.addEventListener('click',adicionarProduto)
const Btndeletar = document.getElementById('deletar')
Btndeletar.addEventListener('click', deletarProduto)






