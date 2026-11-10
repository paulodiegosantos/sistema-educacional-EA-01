from django.contrib import admin

# Register your models here.
from .models import Aluno, Curso


admin.site.register(Aluno)
admin.site.register(Curso)