import serializers as serializers

from rest_framework import routers, serializers, viewsets

from resourcesApp.models import Estado, Recurso, Tipo_Recurso


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nombre','descripcion')

class RecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recurso
        fields = ('nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado')

    def create(self, validated_data):
        recurso = super(RecursoSerializer,self).create(validated_data)
        recurso.save()
        return recurso

class TipoRecursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ['id']
        model = Tipo_Recurso
        fields = ('id','nombre')


class RecursoCreate(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields =('nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado')
