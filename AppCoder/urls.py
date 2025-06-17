from django.urls import path
from .views import (
    lista_libros, lista_autores, lista_editoriales, detalle_libro,
    crear_autor, crear_editorial, crear_libro
)

urlpatterns = [
    path('libros/', lista_libros, name='lista_libros'),
    path('autores/', lista_autores, name='lista_autores'),
    path('editoriales/', lista_editoriales, name='lista_editoriales'),
    path('libro/<int:libro_id>/', detalle_libro, name='detalle_libro'),
    path('crear_autor/', crear_autor, name='crear_autor'),
    path('crear_editorial/', crear_editorial, name='crear_editorial'),
    path('crear_libro/', crear_libro, name='crear_libro'),
]