from django.contrib import admin

# Register your models here.
from .models import Aprendiz,Notas

admin.site.register(Aprendiz)
admin.site.register(Notas)

