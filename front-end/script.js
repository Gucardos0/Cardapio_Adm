
// Link com API
fetch("http://127.0.0.1:8000/produtos")
.then(resposta => resposta.json())
.then(dados =>{
    console.log(dados)
    const contairner = document.getElementById('cards')
    dados.forEach(produto => {
        const card = document.createElement('div')
        card.innerHTML += `
        <h3>${produto.nome}</h3>
        <p>${produto.descricao}</p>
        <img src="${produto.imagem}">g
        <strong>R$ ${produto.preco}</strong>
        
      `
      card.setAttribute('class','card')
      contairner.appendChild(card)
    })
    
})

 .catch(erro => {
    console.error("Erro:", erro)
  });

