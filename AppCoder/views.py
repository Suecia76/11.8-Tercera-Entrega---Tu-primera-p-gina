from django.shortcuts import render, redirect
from .models import Autor, Editorial, Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'AppCoder/libros/lista_libros.html', {'libros': libros})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'AppCoder/autores/lista_autores.html', {'autores': autores})

def lista_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'AppCoder/editoriales/lista_editoriales.html', {'editoriales': editoriales})

def detalle_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    return render(request, 'AppCoder/libros/detalle_libro.html', {'libro': libro})

def crear_autor(request):
    if request.method == 'POST':
        autor = Autor(nombre=request.POST.get('nombre'),
                      nacionalidad=request.POST.get('nacionalidad'),
                      fecha_nacimiento=request.POST.get('fecha_nacimiento'))
        autor.save()
        return render(request, 'AppCoder/autor_creado.html', {'autor': autor})
        
    return render(request, 'AppCoder/crear_autor.html')

def crear_editorial(request):
    if request.method == 'POST':
        editorial = Editorial(
            nombre=request.POST.get('nombre'),
            pais=request.POST.get('pais'),
            fundacion=request.POST.get('fundacion')
        )
        editorial.save()
        return render(request, 'AppCoder/editoriales/editorial_creada.html', {'editorial': editorial})
    return render(request, 'AppCoder/editoriales/crear_editoriales.html')

def crear_libro(request):
    if request.method == 'POST':
        autor_id = request.POST.get('autor')
        editorial_id = request.POST.get('editorial')
        libro = Libro(
            titulo=request.POST.get('titulo'),
            autor=Autor.objects.get(id=autor_id),
            editorial=Editorial.objects.get(id=editorial_id),
            fecha_publicacion=request.POST.get('fecha_publicacion'),
            isbn=request.POST.get('isbn')
        )
        libro.save()
        return render(request, 'AppCoder/libros/libro_creado.html', {'libro': libro})
    return render(request, 'AppCoder/libros/crear_libros.html')