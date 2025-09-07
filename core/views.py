from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/QS.html")

def fq(request):
    return render(request, "core/preguntas.html")

def gallery(request):
    return render(request, "core/galeria.html")