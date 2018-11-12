from rest_framework import generics, filters, viewsets

from resourcesApp.models import Responsable
from resourcesApp.serializer import ResponsableSerializer


class ResponsableViewSet(generics.ListAPIView):
    queryset = Responsable.objects.all().order_by('id')
    serializer_class = ResponsableSerializer
