from enum import unique
from django import forms
from django.forms.widgets import NumberInput

listaGenero=[('Femenino', 'Femenino'),
    ('Masculino', 'Masculino')]
    

listaInstrumenos= [('Piano', 'Piano'),
    ('Violín', 'Violín'),
    ('Flauta','Flauta'),
    ('Violonchelo','Violonchelo'),
    ('Bandoneón','Bandoneón')]

listaPaises = [('Argentina', 'Argentina'),
    ('España', 'España'),
    ('México','México'),
    ('Estados Unidos','Estados Unidos'),
    ('Venezuela','Venezuela'),
    ('Colombia','Colombia'),
    ('Londres','Londres'),
    ('Alemania','Alemania')]    


class usuarioForm(forms.Form):
    email = forms.EmailField(max_length=100, label='Email')
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    passwordRepetir = forms.CharField(max_length=8, label='Repetir Password', widget=forms.PasswordInput)

       
    def clean_passwordRepetir(self):
        password= self.cleaned_data.get('password')
        passwordRepetir = self.cleaned_data.get('passwordRepetir')

        if password != passwordRepetir:
            raise forms.ValidationError("Contraseñas no coinciden.")
        return passwordRepetir    


class DatosUsuarioForm(forms.Form):
    #idUsuario=forms.IntegerField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    idUsuario=forms.IntegerField(widget = forms.HiddenInput())
    nombre= forms.CharField(max_length=100)
    apellido= forms.CharField(max_length=100)
    birthdate= forms.DateField(label='Fecha Nacimiento', widget=NumberInput(attrs={'type': 'date'}))
    telefono= forms.CharField(label='Teléfono', max_length=100)
    genero= forms.CharField(label='Género', widget=forms.Select(choices=listaGenero))

class MusicosForm(forms.Form):
    nombre= forms.CharField(max_length=100)
    apellido= forms.CharField(max_length=100)
    instrumento= forms.CharField(label='Instrumento', widget=forms.Select(choices=listaInstrumenos))
    fecha_nacimiento= forms.DateField(label='Fecha Nacimiento', widget=NumberInput(attrs={'type': 'date'}))
    fecha_fallecimiento= forms.DateField(label='Fecha Fallecimiento', widget=NumberInput(attrs={'type': 'date'}))
    acercade= forms.CharField (label='Acerca de', widget= forms.Textarea)
    
class ContactoForm(forms.Form):
    nombre= forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100, label='Email')
    pais= forms.CharField(label='Paises', widget=forms.Select(choices=listaPaises))
    descripcion= forms.CharField (label='Breve Mensaje', widget= forms.Textarea)    

class BuscarMusicoForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")    