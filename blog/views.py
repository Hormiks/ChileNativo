from django.shortcuts import render

# Create your views Imagen.
def gallery(request):
    return render(request, "blog/galeria.html")

def news(request):
    return render(request, "blog/noticias.html")