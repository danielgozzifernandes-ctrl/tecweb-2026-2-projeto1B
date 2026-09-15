# Get-it

Aplicação de anotações (estilo Post-it) feita em Django para o Projeto 1B de Tecnologias Web.

## Funcionalidades

- Criar, listar, editar e apagar anotações
- Validação do formulário (título e conteúdo obrigatórios)
- Cada anotação pode ter nenhuma, uma ou várias tags (digitadas separadas por vírgula);
  página com a lista de tags e página com as anotações de cada tag
- Página 404 personalizada

## Rodando com PostgreSQL no Docker (Tarefa 03)

```bash
docker compose up -d
python manage.py migrate
python manage.py runserver
```

O banco é escolhido pela variável de ambiente `DATABASE_URL`. Para o Postgres local
do `docker-compose.yml`, coloque no arquivo `.env`:

```
DATABASE_URL=postgres://getituser:getitsenha@localhost:5432/getit
```

## Deploy no Render (Tarefa 04)

1. Criar um PostgreSQL no Render (plano gratuito) e copiar a **External Database URL**.
2. Criar um Web Service apontando para este repositório.
3. Em *Environment*, criar a variável `DATABASE_URL` com a External Database URL.
4. Start Command:

```
python manage.py migrate && python manage.py collectstatic && gunicorn getit.wsgi:application
```

Link da aplicação: https://tecweb-2026-2-projeto1b-6dop.onrender.com
