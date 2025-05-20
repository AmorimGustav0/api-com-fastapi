# Must Watch - API com FastAPI

Este projeto é uma API RESTful construída com **FastAPI** que gerencia um banco de dados de séries, atores e avaliações. Ele permite operações CRUD em múltiplas tabelas, com rotas dinâmicas e conexão ao banco de dados MySQL.

## 📁 Estrutura do Projeto

```
API-COM-FASTAPI/
├── app/
│   ├── main.py                 # Inicializa a aplicação e inclui as rotas
│   ├── routes/
│   │   └── series.py           # Define as rotas da API
│   ├── models/
│   │   ├── database.py         # Gerencia a conexão com o banco de dados
│   │   └── serie.py            # Lógica de CRUD e regras de negócio
│   └── data/
│       └── must_watch.sql      # Script SQL com a estrutura do banco
├── .env                        # Variáveis de ambiente reais (não versionado)
├── .env.example                # Exemplo de variáveis de ambiente
├── requirements.txt            # Dependências do projeto
└── teste.py                    # Script de testes (opcional)
```

## ⚙️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/AmorimGustav0/api-com-fastapi.git
cd api-com-fastapi
```

### 2. Crie o ambiente virtual
```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual
- **Windows**:
```bash
.venv\Scripts\activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Configure o arquivo `.env`
Crie um arquivo `.env` na raiz com base no `.env.example`:

```
DB_HOST=localhost
DB_USER=root
DB_PSWD=admin
DB_NAME=must_watch
```

## 📌 Funcionalidades da API

### 📁 Rotas Dinâmicas (CRUD)
- `GET /{table_name}`: lista todos os registros da tabela.
- `GET /{table_name}/{nome}`: busca um item pelo nome.
- `POST /{table_name}`: cria um novo item.
- `PUT /{table_name}/{nome}`: atualiza um item existente.
- `DELETE /{table_name}/{nome}`: deleta um item.

### 👥 Relacionar Atores com Séries
- `POST /ator_serie/completo`: vincula um ator a uma série, informando nome, título e personagem.

**Exemplo de corpo da requisição**:
```json
{
  "nome_ator": "Bryan Cranston",
  "titulo": "Breaking Bad",
  "personagem": "Walter White"
}
```

## 🗃️ Tabelas e Estrutura

O arquivo `must_watch.sql` contém a estrutura do banco de dados com as seguintes tabelas:

- `serie`
- `categoria`
- `ator`
- `ator_serie`
- `avaliacao_serie`
- `motivo_assistir`

