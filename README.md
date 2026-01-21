#  Cardápio Digital com Painel Admin

Este projeto é um **cardápio digital** com sistema de gerenciamento de produtos, desenvolvido para praticar **Full Stack Web Development** usando **HTML, CSS, JavaScript, Python (FastAPI)** e **SQLite**.

O sistema permite visualizar os produtos no site principal e gerenciá-los por meio de uma página administrativa.

---

##  Funcionalidades

### Usuário (Front-end)
- Visualização dos produtos  
- Nome, descrição, preço e imagem  
- Layout responsivo  
- Consumo da API via `fetch`  

### Administrador (Painel /adm)
- Adicionar produtos  
- Deletar produtos  
- Inserir imagens via URL  
- Comunicação direta com o banco de dados  

### Back-end
- API criada com **FastAPI**  
- Banco de dados **SQLite**  
- Rotas REST:  
  - `GET /produtos`  
  - `POST /produtos`  
  - `DELETE /produtos/{id}`  
- CORS configurado para integração com o front-end  

---

## 🛠️ Tecnologias Utilizadas

- HTML5  
- CSS3  
- JavaScript (Fetch API)  
- Python  
- FastAPI  
- SQLite  
- Git & GitHub  

---

## 📂 Estrutura do Projeto
 /front-end

index.html

adm.html

script.js

adm.js

style.css

/back-end

app.py

database.py

SQLite(3).db


---

##  Como Rodar o Projeto

### 1. Instalar dependências
```bash
pip install fastapi uvicorn

uvicorn app:app --reload
```
---
## Abrir no navegador

# Cardápio:
http://127.0.0.1:5500/front-end/index.html

# Painel Admin:
http://127.0.0.1:5500/front-end/adm.html

## Aprendizados

Neste projeto foram praticados:

Integração Front-end + Back-end

Criação de API REST

Manipulação de banco de dados

Consumo de API com JavaScript

Organização de projeto Full Stack

# Autor

Desenvolvido por Gustavo Cardoso
Projeto de estudo em desenvolvimento web.











