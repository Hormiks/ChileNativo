from django.db import models

ESTADOS = [
    ('EX', 'Extinta'),
    ('EW', 'Extinta en Estado Silvestre'),
    ('CR', 'En Peligro Crítico'),
    ('EN', 'En Peligro'),
    ('VU', 'Vulnerable'),
    ('NT', 'Casi Amenazada'),
    ('LC', 'Preocupación Menor'),
    ('DD', 'Datos Insuficientes'),
    ('NA', 'No evaluada'),
]

class Especie(models.Model):
    nombre_comun = models.CharField(max_length=150, blank=True)
    nombre_cientifico = models.CharField(max_length=150, unique=True)
    tipo = models.CharField(max_length=20, choices=[('fauna', 'Fauna'), ('flora', 'Flora')])
    zona = models.CharField(max_length=150, blank=True)
    estado_conservacion = models.CharField(max_length=2, choices=ESTADOS, default='NA')
    imagen_url = models.URLField(blank=True)

    def __str__(self):
        return self.nombre_comun or self.nombre_cientifico


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    imagen_url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


class Faq(models.Model):
    pregunta = models.CharField(max_length=250)
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta
