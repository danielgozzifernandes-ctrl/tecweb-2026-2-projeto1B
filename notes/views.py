from django.shortcuts import get_object_or_404, redirect, render

from .models import Note, Tag


def _get_tags(texto):
    """Transforma o texto digitado no formulário numa lista de tags.

    O usuário separa os nomes por vírgula ("casa, prova, urgente"). Tags que já
    existem são reaproveitadas e as novas são criadas. Devolve uma lista vazia
    quando o campo vem em branco (anotação sem tag).
    """
    tags = []
    for nome in texto.split(','):
        nome = nome.strip()
        if not nome:
            continue

        tag, _ = Tag.objects.get_or_create(nome=nome)
        if tag not in tags:
            tags.append(tag)

    return tags


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo', '').strip()
        content = request.POST.get('detalhes', '').strip()
        tags_texto = request.POST.get('tags', '')

        if not title or not content:
            context = {
                'notes': Note.objects.all(),
                'erro': 'Preencha o título e o conteúdo da anotação.',
                'titulo': title,
                'detalhes': content,
                'tags': tags_texto,
            }
            return render(request, 'notes/index.html', context)

        note = Note.objects.create(title=title, content=content)
        note.tags.set(_get_tags(tags_texto))
        return redirect('index')

    return render(request, 'notes/index.html', {'notes': Note.objects.all()})


def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        title = request.POST.get('titulo', '').strip()
        content = request.POST.get('detalhes', '').strip()
        tags_texto = request.POST.get('tags', '')

        if not title or not content:
            context = {
                'note': note,
                'erro': 'Preencha o título e o conteúdo da anotação.',
                'titulo': title,
                'detalhes': content,
                'tags': tags_texto,
            }
            return render(request, 'notes/edit.html', context)

        note.title = title
        note.content = content
        note.save()
        note.tags.set(_get_tags(tags_texto))
        return redirect('index')

    tags_atuais = ', '.join(tag.nome for tag in note.tags.all())
    return render(request, 'notes/edit.html', {'note': note, 'tags': tags_atuais})


def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.delete()
        return redirect('index')

    return render(request, 'notes/delete.html', {'note': note})


def tags_list(request):
    return render(request, 'notes/tags_list.html', {'tags': Tag.objects.all()})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': tag.notes.all()})
