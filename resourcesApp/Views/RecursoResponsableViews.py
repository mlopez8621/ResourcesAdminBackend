from typing import re

from django.http.response import HttpResponse
from rest_framework import generics, filters, viewsets, serializers, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from resourcesApp.models import Recurso_Responsable
from resourcesApp.serializer import RecursoResponsableSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# @csrf_exempt
# def recursoResponsable_list(request):
#     if request.method == 'GET':
#         recursoResponsable = Recurso_Responsable.objects.all()
#         serializer = RecursoResponsableSerializer(recursoResponsable, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serialized = RecursoResponsableSerializer(data=data)
#         if serialized.is_valid():
#             serialized.update()
#             return JSONResponse(serialized.data, status=status.HTTP_201_CREATED)
#         else:
#             return JSONResponse(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class RecursoResponsableViewSet(generics.ListAPIView):
    queryset = Recurso_Responsable.objects.all()
    serializer_class = RecursoResponsableSerializer

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def recursoResponsable_list(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        recursoResponsable = Recurso_Responsable.objects.get(pk = pk)
    except Recurso_Responsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecursoResponsableSerializer(recursoResponsable)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("Entro al put")
        print("request.data:", request.data)

        #request.data={'id': 1, 'responsable': 2, 'rescursos': 1}

        data = request.data


        print("request.data2:", data)
        serializer = RecursoResponsableSerializer(recursoResponsable, data=request.data)

        print("idResponsable:", serializer)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recursoResponsable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)