# Get-it

Aplicação de anotações (estilo Post-it) feita em Django para o Projeto 1B de
Tecnologias Web.

**Aplicação publicada:** https://tecweb-2026-2-projeto1b-6dop.onrender.com

## Tarefas

| Tarefa | O que foi feito |
|---|---|
| 01 — CRUD em Django | Criar, listar, editar e apagar anotações |
| 02 — Sistema de tags | Cada anotação pode ter uma tag (relação *many-to-one*) |
| 03 — PostgreSQL no Docker | Banco em container, configurado no `docker-compose.yml` |
| 04 — Deploy | Publicado no Render (link acima) |

Além do pedido nas tarefas: validação do formulário (não deixa criar anotação sem
título ou sem conteúdo), página de confirmação antes de apagar e página 404
personalizada.

### Rotas

| Rota | Função |
|---|---|
| `/` | Lista as anotações e o formulário de criação |
| `/edit/<id>` | Edita uma anotação (Salvar ou Cancelar) |
| `/delete/<id>` | Confirma e apaga uma anotação |
| `/tags/` | Lista todas as tags |
| `/tags/<id>/` | Anotações de uma tag |

## Rodando localmente

Suba o PostgreSQL em container:

```bash
docker compose up -d
```

Crie um arquivo `.env` na raiz do projeto (veja o `.env.example`):

```
DATABASE_URL=postgres://getituser:getitsenha@localhost:5432/getit
```

E rode o projeto:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

A aplicação fica em http://localhost:8000/.

## Deploy

Feito no Render, seguindo o handout:

- O banco é um PostgreSQL do próprio Render; a *External Database URL* fica na
  variável de ambiente `DATABASE_URL` do serviço (não está no código porque o
  repositório é público).
- Start Command:

```
python manage.py migrate && python manage.py collectstatic && gunicorn getit.wsgi:application
```

## Branches

| Branch | Conteúdo |
|---|---|
| `main` | Projeto completo: tarefas 01 a 04 |
| `docker-postgres` | Branch onde as tarefas 03 e 04 foram desenvolvidas, antes do merge |
| `tags-many-to-many` | **Extra:** tags *many-to-many* — uma anotação pode ter várias tags, digitadas separadas por vírgula |

A `main` mantém a relação *many-to-one* porque é o que a tarefa 02 pede. A versão
com *many-to-many* está na branch `tags-many-to-many`.
