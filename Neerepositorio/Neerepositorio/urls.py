"""Neerepositorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from tomlkit import document
from core import views as core_views
from portfolio.url import projectpatterns
#from portfolio import views as portfolio_views
from messenger.urls import messenger_patterns
from django.conf import settings
from profiles.urls import profiles_patterns
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('Proyectos/', include(projectpatterns)),
    #path('',core_views.home, name="home"),
    #path('proyectos/',portfolio_views.proyectos, name="proyectos"),
    #path('perfil/',core_views.perfil, name="perfil"),
    #path('about-me/',core_views.about, name="about-me"),
    #path('detalle/', portfolio_views.detalle, name="detalle"),
    #path('detalle/<int:project_id>/', portfolio_views.detalle, name="detalle"),
    #path('', portfolio_views.proyectos, name="proyectos"),
    #path('detalle/', portfolio_views.detalle, name="detalle"),
    path('admin/', admin.site.urls),
    #path de Autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    path('messenger/', include(messenger_patterns)),
    
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)