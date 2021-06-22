from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('nuevo/', views.new),
    path('cargarart/', views.ArticulosList),
    path('eliminarArticulo/<id>', views.EliminarArticulo),
]
