
from rest_framework import generics, filters, viewsets

from resourcesApp.models import Recurso
from resourcesApp.serializer import RecursoSerializer


class RecursoViewSet(viewsets.ModelViewSet):

    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('=estado','nombres')