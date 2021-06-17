from django.db import models

# Create your models here.
class Articulo(models.Model):
  titulo = models.CharField(max_length=100, blank=False, null=False)
  descripcion = models.CharField(max_length=250, blank=False, null=False)
  fecha_creacion = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'articulos' #nombre de la tabla
    verbose_name = 'articulos' #nombre en el sitio administrativo
    ordering = ['id'] 

  def __str__(self):
    return self.titulo