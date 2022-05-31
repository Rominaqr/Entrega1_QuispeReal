from ctypes.wintypes import MSG
from email import message
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.template import loader
from django.urls import is_valid_path
from WebApp.forms import MusicosForm, usuarioForm, DatosUsuarioForm, ContactoForm, BuscarMusicoForm
from WebApp.models import Contacto, DatosUsuario, Usuario, Musicos
from django.contrib import messages


# Create your views here.

def index(request):
    musicos_tbl = Musicos.objects.all()
    template = loader.get_template('WebApp/index.html')
    context = {
        'musico': musicos_tbl,
    }
    return HttpResponse(template.render(context, request))


def altaUsuario(request):
    if request.method == "POST":
        form = usuarioForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                 
                #verifico si existe el mail envio mensaje de error
                mail_usr = Usuario.objects.filter(email=email) 
                if mail_usr:
                    messages.error(request,'Email ya registrado')
                else:
                    usuario = Usuario(email=email, password = password)
                    usuario.save()
                    messages.success(request,'El usuario se agrego correctamente')
                    idUsr = usuario.id
                    return HttpResponseRedirect("/WebApp/datosUsuario/%s" %idUsr)
                
            except (RuntimeError):
                messages.error(request,'Se produjo un error al guardar')    
        else:
            for msg in form.errors:
                messages.error(request, form.errors[msg])

            return HttpResponseRedirect("/WebApp/registrar/")
            
         
    elif request.method == "GET":
        form = usuarioForm()
    else:
        return HttpResponseBadRequest("Error, no conzco el metodo para el request")

    #return HttpResponseRedirect("/WebApp/registrar/")
    return render(request, 'WebApp/altaUsuario.html', {'form': form}) 
    


def new_func(form):
    return form.instance.id
    

def altaDatosUsuario(request, idUsuario):
    if request.method == "POST":
        form = DatosUsuarioForm(request.POST)
        if form.is_valid():
                try:
                    idUsuario=form.cleaned_data['idUsuario']
                    nombre= form.cleaned_data['nombre']
                    apellido= form.cleaned_data['apellido']
                    birthdate= form.cleaned_data['birthdate']
                    telefono= form.cleaned_data['telefono']
                    genero= form.cleaned_data['genero']

                    DatosUsuario(idUsuario=idUsuario, nombre = nombre, apellido=apellido, birthdate=birthdate, telefono=telefono, genero=genero).save()
                    messages.success(request,'Los datos se han guardado con exito, registración finalizada')
                except (RuntimeError):
                    messages.error(request,'Se produjo un error al guardar')    
                #return HttpResponseRedirect("/WebApp/datosUsuario/%s" %idUsuario)
                return HttpResponseRedirect("/WebApp/registrar/")
            
    elif request.method == "GET":
        form = DatosUsuarioForm(initial= {'idUsuario':idUsuario,'nombre':' ','apellido':' ','birthdate':' ','telefono':' ','genero':' ' })
         
    else:
        return HttpResponseBadRequest("Error no conzco ese método para esta request")

    
    return render(request, 'WebApp/altaDatosUsuario.html', {'form': form})
        

def inicioMusicos(request):
    musicos = Musicos.objects.all()
    template = loader.get_template('WebApp/inicioMusicos.html')
    context = {
        'musicos': musicos,
    }
    return HttpResponse(template.render(context, request))


def altaMusicos(request):
    if request.method == "POST":
        form = MusicosForm(request.POST)
        if form.is_valid():
            try:
                nombre=form.cleaned_data['nombre']
                apellido=form.cleaned_data['apellido']
                instrumento= form.cleaned_data['instrumento']
                fecha_nacimiento= form.cleaned_data['fecha_nacimiento']
                fecha_fallecimiento= form.cleaned_data['fecha_fallecimiento']
                acercade= form.cleaned_data['acercade']
                Musicos(nombre=nombre, apellido = apellido, instrumento=instrumento, fecha_nacimiento=fecha_nacimiento, fecha_fallecimiento=fecha_fallecimiento, acercade=acercade).save()
                messages.success(request,'Los datos se han guardado con exito')
            except (RuntimeError):
                messages.error(request,'Se produjo un error al guardar')
            return HttpResponseRedirect("/WebApp/musicosIngresar/")       
        else:
            messages.error(request,'Se produjo un error al guardar')
            return HttpResponseRedirect("/WebApp/musicosIngresar/")  
    elif request.method == "GET":
        form = MusicosForm()
         
    else:
        return HttpResponseBadRequest("Error no conozco ese método para esta request")

    
    return render(request, 'WebApp/altaMusicos.html', {'form': form})

def buscarMusico(request):
     
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarMusicoForm(request.GET)
        if form_busqueda.is_valid():
            musico = Musicos.objects.filter(apellido__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'WebApp/buscarMusico.html', {"musico": musico, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarMusicoForm()
        return render(request, 'WebApp/buscarMusico.html', {"form_busqueda": form_busqueda})
        
    

def altaContacto (request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            try:
                nombre=form.cleaned_data['nombre']
                apellido=form.cleaned_data['apellido']
                email = form.cleaned_data['email']
                pais= form.cleaned_data['pais']
                descripcion= form.cleaned_data['descripcion']
                Contacto(nombre=nombre, apellido = apellido, email=email, pais=pais, descripcion=descripcion).save()
                messages.success(request,'El mensaje se ha enviado con éxito, nos contactaremos a la brevedad.')
            except (RuntimeError):
                messages.error(request,'Se produjo un error al guardar')
            return HttpResponseRedirect("/WebApp/contacto/")       
        else:
            messages.error(request,'Se produjo un error al guardar')
            return HttpResponseRedirect("/WebApp/contacto/")  
    elif request.method == "GET":
        form = ContactoForm()
         
    else:
        return HttpResponseBadRequest("Error no conozco ese método para esta request ")+ request

    
    return render(request, 'WebApp/contacto.html', {'form': form})


