import serializers as serializers

from rest_framework import routers, serializers, viewsets


from resourcesApp.models import Estado, Recurso, Responsable, Recurso_Responsable, Recurso_Comentario, \
    TipoRecurso


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nombre','descripcion')

class RecursoSerializer(serializers.ModelSerializer):
    nombre_estado = serializers.CharField(source='estado.nombre', read_only=True)
    nombre_tipo = serializers.CharField(source='tipoRecurso.nombre', read_only=True)
    class Meta:
        model = Recurso
        fields = ('id', 'nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado', 'nombre_estado', 'nombre_tipo')

    def create(self, validated_data):
        recurso = super(RecursoSerializer,self).create(validated_data)
        recurso.save()
        return recurso

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
        model = TipoRecurso
        fields = ('id','nombre')

class RecursoCreate(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields =('nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado')

class RecursoComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso_Comentario
        fields = '__all__'