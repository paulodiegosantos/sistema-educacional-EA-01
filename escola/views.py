from django.shortcuts import render
from .models import Aluno, Curso

# Create your views here.
def listar_alunos(request):
    alunos = Aluno.objects.all()

    return render(request, 'escola/alunos.html', {
        'alunos': alunos
    })

def listar_cursos(request):
    cursos = Curso.objects.all()

    return render(request, 'escola/cursos.html',{
        'cursos': cursos
    })

def exibir_home(request):
    return render(request, 'escola/home.html')