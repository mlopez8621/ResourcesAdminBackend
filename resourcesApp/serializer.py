import serializers as serializers

from rest_framework import routers, serializers, viewsets

from resourcesApp.models import Estado, Recurso, Responsable, Recurso_Responsable


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nombre','descripcion')

class RecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recurso
        fields = ('nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado')

class ResponsableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsable
        fields = '__all__'

class RecursoResponsableSerializer(serializers.ModelSerializer):
   #responsable = serializers.StringRelatedField(many=True)
    #recursoObj = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recurso_Responsable
        fields = '__all__'

