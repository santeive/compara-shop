from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 245 caracteres como máximo y debe ser válido")

    # Redefinimos la clase meta
    # La clase UserCreationFormWithEmail se importa en el views.py
    class Meta:
        #Email ya es un campo de user
        model = User
        fields = ("username", "email", "password1", "password2")
        #Si nosotros sobre escribimos el campo widgets, estariamos perdiendo las validaciones
        # y configuraciones que ya tienen nuestro formulario

    #Toto metodo de una clase recibe un self
    #ESTA VALIDACION COMPRUEBA SI EXISTE UAN EMAIL CON ESA DIRECCION ANTES DE GUARDARLO
    def clean_email(self):
        email = self.cleaned_data.get("email") # Recuperamos el email que estamos validando
        if User.objects.filter(email = email).exists(): #Devuelve un query set o lista vacia
            raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 245 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']
    
    def clean_email(self):
        email = self.cleaned_data.get("email") 
        # Verificamos si el email se ha modificado
        if 'email' in self.changed_data:
            #Es una lista de todos los campos que se han editado en el formulario
            if User.objects.filter(email = email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email
