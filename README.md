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

O `settings.py` lê o `.env` automaticamente. A ordem de escolha do banco é:
`DATABASE_URL` (deploy) → `DB_NAME`/`DB_USER`/... (Postgres local) → SQLite.

## Deploy

O projeto já vem com `render.yaml`, `build.sh` e `Procfile`. No [Render](https://render.com):

1. New + → Blueprint → conectar este repositório (branch `docker-postgres`).
2. O blueprint cria o banco PostgreSQL e o serviço web; `SECRET_KEY` é gerada e
   `DEBUG=False` já vem definido.
3. Ao terminar, colar aqui o link:

Link da aplicação: _(a adicionar)_
