from django.shortcuts import get_object_or_404, redirect, render


from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo', '').strip()
        content = request.POST.get('detalhes', '').strip()

        if not title or not content:
            all_notes = Note.objects.all()
            context = {
                'notes': all_notes,
                'erro': 'Preencha o título e o conteúdo da anotação.',
                'titulo': title,
                'detalhes': content,
            }
            return render(request, 'notes/index.html', context)

        Note.objects.create(title=title, content=content)
        return redirect('index')

    all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})


def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        title = request.POST.get('titulo', '').strip()
        content = request.POST.get('detalhes', '').strip()

        if not title or not content:
            context = {
                'note': note,
                'erro': 'Preencha o título e o conteúdo da anotação.',
                'titulo': title,
                'detalhes': content,
            }
            return render(request, 'notes/edit.html', context)

        note.title = title
        note.content = content
        note.save()
        return redirect('index')

    return render(request, 'notes/edit.html', {'note': note})


def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.delete()
        return redirect('index')

    return render(request, 'notes/delete.html', {'note': note})
