# 📁 Controllers

A pasta **controllers** é responsável por armazenar os arquivos que lidam com a lógica das rotas da aplicação.  
Aqui ficam as funções que recebem requisições, processam dados e retornam respostas (páginas HTML, JSON, redirecionamentos, etc).

Este diretório representa a camada **Controller** do padrão MVC.

---

## 📌 Função desta pasta

- Controlar o fluxo da aplicação  
- Receber e tratar requisições do usuário  
- Fazer a ponte entre **modelos (models)** e **templates (views)**  
- Renderizar páginas HTML  
- Redirecionar ações (criar, editar, excluir, listar, etc)

---

## 📄 Arquivos

### `views.py`
Arquivo principal do diretório.  
Nele você definirá:

- As rotas (`@app.route`)
- Funções que cada rota executa
- Chamadas ao banco de dados via `models`
- Retorno das páginas HTML renderizadas


