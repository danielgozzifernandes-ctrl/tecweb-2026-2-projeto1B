# Get-it

Aplicação de anotações (estilo Post-it) feita em Django para o Projeto 1B de Tecnologias Web.

## Funcionalidades

- Criar, listar, editar e apagar anotações
- Validação do formulário (título e conteúdo obrigatórios)
- Cada anotação pode ter uma tag; página com a lista de tags e página com as anotações de cada tag
- Página 404 personalizada

## Rodando localmente

```bash
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

A aplicação fica em http://localhost:8000/.
