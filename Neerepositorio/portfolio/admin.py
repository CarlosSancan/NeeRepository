from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    class Media:
        css = {
            'all': ('portfolio/css/custom_ckeditor.css',)
        }


admin.site.register(Project, ProjectAdmin )
