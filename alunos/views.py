from django.shortcuts import render, redirect
from .models import Aluno  # Importe o model Aluno
from .forms import AlunoForm

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()

    return render(request, 'alunos/cadastrar_aluno.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.all()  # Use o model Aluno
    return render(request, 'alunos/listar_alunos.html', {'alunos': alunos})
