from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('', views.exibir_home, name='home')
]