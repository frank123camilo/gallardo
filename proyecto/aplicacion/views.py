from django.shortcuts import render

# Create your views here.



def inicio(request): # se define una funcion que toma un parametro request
    return render(request, 'inicio.html')



