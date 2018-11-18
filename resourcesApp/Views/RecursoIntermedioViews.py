from django.http.response import HttpResponse
from rest_framework import generics, filters, viewsets, serializers, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from resourcesApp.models import Recurso_Intermedio
from resourcesApp.serializer import Recurso, RecursoIntermedioSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class RecursoIntermedioViewSet(generics.ListAPIView):
    serializer_class = RecursoIntermedioSerializer

    def get_queryset(self):
        queryset = Recurso_Intermedio.objects.all()
        idRecurso = self.request.query_params.get('idRecurso', None)
        if idRecurso:
            queryset = queryset.filter(recursoPrincipal=idRecurso)

        return queryset

