# 📝 Gerenciador de Tarefas – Aplicação Flask

Este repositório apresenta uma aplicação web simples para controle de tarefas, desenvolvida com **Flask**.  
O projeto demonstra na prática o uso de rotas, templates, modelos de dados e arquivos estáticos.

A aplicação permite adicionar, visualizar, alterar e excluir tarefas, mantendo tudo salvo em um banco SQLite através do **SQLAlchemy**.

---

## 📂 Arquitetura do Projeto

A estrutura foi organizada para separar responsável de cada parte da aplicação:

```
/projeto_final
│
├── /controllers
│   └── views.py
│
├── /models
│   └── modelo.py   (classes a serem criadas)
│
├── /templates
│   ├── index.html
│   └── outras páginas necessárias
│
├── /static
│   ├── /css
│   │   └── style.css
│   ├── /js
│   │   └── script.js
│   └── /img
│       └── (imagens usadas no projeto)
│
├── README.md
└── run.py

````

---

## 🚀 Funcionalidades Principais

- Criar novas tarefas  
- Listar todas as tarefas salvas  
- Atualizar informações  
- Remover registros  
- Interface básica com CSS e JavaScript  

---

## 👥 Autores

* Miguel Gomes Maia
* Kaynara Terezinha de Jesus Silva Queiroz
* Eric da Silva Ramos
