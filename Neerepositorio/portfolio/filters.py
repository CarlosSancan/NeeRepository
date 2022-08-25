import django_filters
from .models import Project

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Project
        fields = {'title': ['exact'], 'categoria': [
            'exact']}