import serializers as serializers

from rest_framework import routers, serializers, viewsets


from resourcesApp.models import Estado, Recurso, Responsable, Recurso_Responsable, Tipo_Recurso


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nombre','descripcion')

class TipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Recurso
        fields = '__all__'

class RecursoSerializer(serializers.ModelSerializer):
    #estado = serializers.StringRelatedField(many=True, read_only=True)
    tipoRecurso = TipoRecursoSerializer(many=True, read_only=True)

    class Meta:
        model = Recurso
        fields = ('nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado')

class ResponsableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsable
        fields = '__all__'

class RecursoResponsableSerializer(serializers.ModelSerializer):
    responsable = serializers.StringRelatedField(read_only='True')
    rescursos = serializers.StringRelatedField(read_only='True')

    class Meta:
        model = Recurso_Responsable
        fields = '__all__'

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

