from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters, viewsets, serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from resourcesApp.models import Recurso, Tipo_Recurso, Control_Comentarios
from resourcesApp.serializer import RecursoSerializer, TipoRecursoSerializer, RecursoComentarioSerializer


@csrf_exempt
def recursos_list(request):
    if request.method == 'GET':
        recurso = Recurso.objects.all().order_by('id')
        serializer = RecursoSerializer(recurso, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = RecursoSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JSONResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JSONResponse(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class RecursoViewSet(generics.ListAPIView):
    serializer_class = RecursoSerializer

    def get_queryset(self):
        queryset = Recurso.objects.all()
        estado = self.request.query_params.get('estado',None)
        id = self.request.query_params.get('id',None)
        if id:
            queryset = queryset.filter(id=id)
        if estado:
            queryset = queryset.filter(estado_id=estado)

        return queryset


class TipoRecursoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Recurso.objects.all()
    serializer_class = TipoRecursoSerializer

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_resources(request):
    serialized = RecursoSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class recursos_comentarios(generics.ListAPIView):
    serializer_class = RecursoComentarioSerializer
    def get_queryset(self):
        queryset = Control_Comentarios.objects.all()
        idRecurso = self.request.query_params.get('idRecurso',None)
        if idRecurso:
            queryset = queryset.filter(idRecurso=idRecurso)

        return queryset