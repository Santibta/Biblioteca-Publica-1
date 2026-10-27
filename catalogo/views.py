from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Usuario
from .forms import LibroForm, UsuarioForm
from django.db.models import Q

def lista_libros(request):
    busqueda = request.GET.get('buscar', '').strip()

    libros = Libro.objects.all().order_by('titulo')

    if busqueda:
        libros = libros.filter(
            Q(titulo__icontains=busqueda) |
            Q(autor__icontains=busqueda)
        )

    return render(request, 'catalogo/lista_libros.html', {
        'libros': libros,
        'busqueda': busqueda,
    })


def crear_libro(request):
    if request.method == 'POST':
        formulario = LibroForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_libros')
    else:
        formulario = LibroForm()

    return render(request, 'catalogo/formulario_libro.html', {
        'formulario': formulario,
        'titulo_pagina': 'Registrar libro',
    })


def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        formulario = LibroForm(request.POST, instance=libro)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_libros')
    else:
        formulario = LibroForm(instance=libro)

    return render(request, 'catalogo/formulario_libro.html', {
        'formulario': formulario,
        'titulo_pagina': 'Editar libro',
    })


def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'catalogo/confirmar_eliminacion.html', {
        'libro': libro,
    })
def lista_usuarios(request):
    busqueda = request.GET.get('buscar', '').strip()
    usuarios = Usuario.objects.all().order_by('nombre')

    if busqueda:
        usuarios = usuarios.filter(
            Q(nombre__icontains=busqueda) |
            Q(documento__icontains=busqueda) |
            Q(correo__icontains=busqueda)
        )

    return render(request, 'catalogo/lista_usuarios.html', {
        'usuarios': usuarios,
        'busqueda': busqueda,
    })


def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')
    else:
        formulario = UsuarioForm()

    return render(request, 'catalogo/formulario_usuario.html', {
        'formulario': formulario,
        'titulo_pagina': 'Registrar usuario',
    })


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, instance=usuario)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')
    else:
        formulario = UsuarioForm(instance=usuario)

    return render(request, 'catalogo/formulario_usuario.html', {
        'formulario': formulario,
        'titulo_pagina': 'Editar usuario',
    })


def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

    return render(request, 'catalogo/confirmar_eliminacion_usuario.html', {
        'usuario': usuario,
    })

def dashboard(request):
    return render(request, 'catalogo/dashboard.html')
