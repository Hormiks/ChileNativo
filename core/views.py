from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/QS.html")

def resources(request):
    return render(request, "core/recursos.html")

