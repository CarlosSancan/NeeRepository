from ast import Return, arg
from contextlib import redirect_stderr
import re
from tkinter.tix import Form
from turtle import pos, title
from unicodedata import category
from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .froms import ProyectoForm


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
         
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class ProfileListView(ListView):
    model = Project
    template_name = 'portfolio\project_list.html'
    

# Create your views here.

class ProyectosListView(ListView):
    model = Project
    paginate_by = 8

class  DetalleDetailView(DetailView):
    #proyecto = get_object_or_404(Project,id=proyect_id)
    #return render(request,"portfolio/detalle.html", {'project':proyecto})
    #detalle|= Project.objects.select_related()
    #return render(request,"portfolio/detalle.html", {'project': detalle})
    model = Project
  
@method_decorator(staff_member_required, name='dispatch') 
class ProyectosCreateView(CreateView):
    model = Project
    success_url = reverse_lazy('portfolio:proyectos')
    form_class = ProyectoForm

@method_decorator(staff_member_required, name='dispatch') 
class ProyectosUpdateView( UpdateView):
    model = Project
    form_class = ProyectoForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('portfolio:update', args=[self.kwargs['pk']]) +'?ok'

@method_decorator(staff_member_required, name='dispatch') 
class ProyectosDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('portfolio:proyectos')

#def home(request):
 #   template_name = 'portfolio\project_list.html'
  #  busqueda= request.GET["busqueda"]
   # project = Project.objects.filter(title__icontains = busqueda)
    #context = {'project' : project

    #}
    #return render(request, template_name, context)
    #queryset = request.GET.get("buscar")
    #project = Project.objects.all()
    #if queryset: 
     # posts = Project.objects.filter(
      #  Q(title__icontains = queryset) |
       # Q(categoria__icontains = queryset)
        #).distinct()
   # return render(request, 'project_list.html',{'Project':project})
   

