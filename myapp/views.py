from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

# Listar todos los libros
def listar_libros(request):
    libros = Libro.objects.all() # pylint: disable=no-member
    return render(request, 'listar_libros.html', {'libros': libros})

# Crear un nuevo libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

# Actualizar un libro
def actualizar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'crear_libro.html', {'form': form})

# Eliminar un libro
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'eliminar_libro.html', {'libro': libro})
