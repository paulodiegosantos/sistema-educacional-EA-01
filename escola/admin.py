from django.contrib import admin

# Register your models here.
from .models import Aluno, Curso, Produto, Usuario


admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Produto)
admin.site.register(Usuario)