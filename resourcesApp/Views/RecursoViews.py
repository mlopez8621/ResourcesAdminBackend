
from rest_framework import generics, filters, viewsets

from resourcesApp.models import Recurso
from resourcesApp.serializer import RecursoSerializer


class RecursoViewSet(generics.ListAPIView):
    serializer_class = RecursoSerializer

    def get_queryset(self):
        queryset = Recurso.objects.all()
        estado = self.request.query_params.get('estado',None)
        if estado:
            queryset = queryset.filter(estado_id=estado)
        return queryset;