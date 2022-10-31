from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
import os

def hola(request):
    ahora = datetime.datetime.now()
    hora = '%s:%s:%s' % (ahora.hour, ahora.minute, ahora.second)
    html = """
<html>
    <body>
       <h1>Hola mundo</h1>
    %s
    </body>
</html>    
    """ % hora
    return HttpResponse(html)

def valores(request):
    """
    Demo para ver variables get.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    if request.method == 'GET':
        valor = request.GET.get('valor', 'No pasaste la variable')
        return HttpResponse(valor)

def regresar_template(request):
    """
    Ejemplo para regresar templates.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    t = 'ejemplo.html'
    c =  {'titulo': 'Ejemplo', 'contenido': 'Hola mundo'}    
    return render(request, t, c)

class Gente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


def mostrar_directorio(request):
    """
    Regresa el contenido de un directorio.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    if request.method == 'GET':
        ruta = request.GET.get('ruta', '')
        if ruta:
            lista = sorted(os.listdir(ruta))
        else:
            lista = []
        frutas = ['manazana', 'pera', 'naranja']
        personas = [{'nombre': 'pepito', 'edad': 12}, {'nombre': 'juanito', 'edad': 14}, {'nombre': 'pedro', 'edad': 15}, Gente('jorge', 16)]    
        c = {'listado': lista, 'titulo': 'Lista archivos', 'personas': personas, 'frutas': frutas}
        t = 'directorio.html'
        return render(request, t, c)

def mostrar_tabla(request):
    """
    Muestra del uso de la etiqueta extends.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    t = 'tabla.html'
    return render(request, t)

def ejemplo_extends(request):
    """
    Muestra del uso de la etiqueta extends.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    t = 'tabla.html'
    return render(request, t)

def mostrar_lista(request):
    """
    Muestra del uso de la etiqueta extends.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    elementos = ["América","Pachuca","Juárez","Pumas","Monterrey","Pachuca"]
    c = {'elementos': elementos}
    t = 'lista.html'
    return render(request, t, c)

def mostrar_tabla(request):
    """
    Muestra del uso de la etiqueta extends.

    Keyword Arguments:
    request -- 
    returns: HttpResponse
    """
    t = 'tabla.html'
    return render(request, t)