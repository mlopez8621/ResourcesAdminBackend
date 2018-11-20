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
@api_view(['POST'])
@permission_classes((AllowAny,))
def crear_comentario(request):
    serializer_class = RecursoComentarioSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

