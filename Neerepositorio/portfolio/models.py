from dataclasses import field
from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from turtle import title, update
from venv import create
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    categoria = models.TextField(verbose_name="Categoria",null=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link= models.URLField (verbose_name="Link de Descarga",null=True, blank=True)
    videos= models.FileField (verbose_name="Video Tutorial",blank=True,null=True,  upload_to="projects" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")



    class Meta: 
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

