from django.urls import path
from . import views

app_name = "apps.comentarios"

urlpatterns = [
    path('Agregar/<int:pk>/',views.Comentar, name='path_comentar'),
  
]