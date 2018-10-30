from rest_framework import generics, filters, viewsets

from resourcesApp.models import Recurso_Responsable
from resourcesApp.serializer import RecursoResponsableSerializer


class RecursoResponsableViewSet(generics.ListAPIView):
    queryset = Recurso_Responsable.objects.all()
    serializer_class = RecursoResponsableSerializer