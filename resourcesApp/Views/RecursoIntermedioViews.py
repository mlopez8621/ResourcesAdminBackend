from rest_framework import generics
from resourcesApp.models import Recurso_Intermedio
from resourcesApp.serializer import  RecursoIntermedioSerializer

class RecursoIntermedioViewSet(generics.ListAPIView):
    serializer_class = RecursoIntermedioSerializer

    def get_queryset(self):
        queryset = Recurso_Intermedio.objects.all()
        idRecurso = self.request.query_params.get('idRecurso', None)
        if idRecurso:
            queryset = queryset.filter(recursoPrincipal=idRecurso).order_by('id')

        return queryset

