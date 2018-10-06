import serializers as serializers

from rest_framework import routers, serializers, viewsets

from resourcesApp.models import Estado, Recurso


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('nombre','descripcion')

class RecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recurso
        fields = ('nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado')