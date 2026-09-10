from django.shortcuts import get_object_or_404, redirect, render

from .models import Note, Tag


def _get_tag(nome):
    """Devolve a tag com esse nome, criando uma nova se ainda não existir.

    Retorna None quando o campo vem vazio (anotação sem tag).
    """
    nome = nome.strip()
    if not nome:
        return None

    tag, _ = Tag.objects.get_or_create(nome=nome)
    return tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo', '').strip()
        content = request.POST.get('detalhes', '').strip()
        tag_nome = request.POST.get('tag', '')

        if not title or not content:
            context = {
                'notes': Note.objects.all(),
                'erro': 'Preencha o título e o conteúdo da anotação.',
                'titulo': title,
                'detalhes': content,
                'tag': tag_nome,
            }
            return render(request, 'notes/index.html', context)

        Note.objects.create(title=title, content=content, tag=_get_tag(tag_nome))
        return redirect('index')

    return render(request, 'notes/index.html', {'notes': Note.objects.all()})


def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        title = request.POST.get('titulo', '').strip()
        content = request.POST.get('detalhes', '').strip()
        tag_nome = request.POST.get('tag', '')

        if not title or not content:
            context = {
                'note': note,
                'erro': 'Preencha o título e o conteúdo da anotação.',
                'titulo': title,
                'detalhes': content,
                'tag': tag_nome,
            }
            return render(request, 'notes/edit.html', context)

        note.title = title
        note.content = content
        note.tag = _get_tag(tag_nome)
        note.save()
        return redirect('index')

    return render(request, 'notes/edit.html', {'note': note})


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
