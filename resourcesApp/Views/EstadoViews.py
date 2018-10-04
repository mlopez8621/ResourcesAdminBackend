
from rest_framework import viewsets

from resourcesApp.models import Estado
from resourcesApp.serializer import EstadoSerializer


class EstadosViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all().order_by('id')
    serializer_class = EstadoSerializer
