
from rest_framework import viewsets

from resourcesApp.models import Estado
from resourcesApp.serializer import EstadoSerializer


class EstadosViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
