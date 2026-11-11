from django.shortcuts import render
from .models import Aluno, Curso, Produto, Usuario
from .forms import ProdutoForm
from rest_framework import generics
from .serializers import UsuarioSerializer

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


def produto_new(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    return render(request, 'escola/produto_form.html', {
        'form': form
    })

def listar_produtos(request):
    produtos = Produto.objects.all()

    return render(request, 'escola/produtos.html',{
        'produtos': produtos
    })

class UsuarioListAPIView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer