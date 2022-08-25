from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from tkinter.ttk import Widget
from django import forms
from .models import Project

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','categoria','link','image','videos']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
            'categoria': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Categoria'}),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link'}),
            
        }
        labels = {
            'title':'','description':'','categoria':'','link':''
        }