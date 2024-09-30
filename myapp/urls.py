from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_libros, name='listar_libros'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('actualizar/<int:id>/', views.actualizar_libro, name='actualizar_libro'),
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]
