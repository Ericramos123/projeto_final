# 📁 Models

A pasta **models** contém todos os arquivos responsáveis pela estrutura do banco de dados da aplicação.  
É aqui que ficam as **classes que representam tabelas**, bem como as relações e operações que envolvem a persistência de dados.

Esta pasta corresponde à camada **Model** do padrão MVC.

---

## 📌 Propósito desta pasta

- Definir **modelos** de dados usando SQLAlchemy  
- Criar tabelas, colunas e relacionamentos  
- Controlar a lógica de persistência (CRUD)  
- Manter a aplicação organizada e separada da lógica de rotas

---

## 📄 Arquivos

### `modelo.py`
Arquivo principal onde suas classes de banco de dados são definidas.

Nele normalmente ficam:

- A instância do SQLAlchemy (`db`)
- As classes que representam as tabelas  
