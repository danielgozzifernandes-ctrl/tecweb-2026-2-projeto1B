# Get-it

Aplicação de anotações (estilo Post-it) feita em Django para o Projeto 1B de Tecnologias Web.

## Funcionalidades

- Criar, listar, editar e apagar anotações
- Validação do formulário (título e conteúdo obrigatórios)
- Cada anotação pode ter uma tag; página com a lista de tags e página com as anotações de cada tag
- Página 404 personalizada

## Rodando localmente (SQLite)

```bash
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

A aplicação fica em http://localhost:8000/.

## Rodando com PostgreSQL (Docker)

```bash
docker compose up -d
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

As credenciais do banco são lidas das variáveis de ambiente (`DB_NAME`, `DB_USER`,
`DB_PASSWORD`, `DB_HOST`, `DB_PORT`). Sem `DB_NAME` definido, o projeto usa o SQLite.

## Deploy

Link da aplicação: _(a adicionar)_
