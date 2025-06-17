from django import forms

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    autor = forms.IntegerField(label="ID del Autor")
    editorial = forms.IntegerField(label="ID de la Editorial")
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    isbn = forms.CharField(max_length=13)

class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class EditorialForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)
    fundacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=False)