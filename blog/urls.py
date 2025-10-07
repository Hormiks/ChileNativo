from django.urls import path
from . import views

app_name = "blog"  

urlpatterns = [
    path("gallery/", views.gallery, name="galeria"),
    path("news/", views.news, name="noticias"),
]
