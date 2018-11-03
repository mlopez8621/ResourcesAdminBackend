import serializers as serializers

from rest_framework import routers, serializers, viewsets


from resourcesApp.models import Estado, Responsable, Recurso_Responsable, \
    Tipo_Recurso, Recurso, Control_Comentarios


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nombre','descripcion')

class RecursoSerializer(serializers.ModelSerializer):
    #nombre_estado = serializers.CharField(source='estado.nombre', read_only=True)
    #nombre_tipo = serializers.CharField(source='tipoRecurso.nombre', read_only=True)

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
    responsable = serializers.CharField(source='responsable.nombres', read_only=True)
    idResponsable = serializers.CharField(source='responsable.id', read_only=True)
    #
    recursos = serializers.CharField(source='rescursos.nombre', read_only=True)
    recursoId = serializers.CharField(source='rescursos.id', read_only=True)
    class Meta:
        model = Recurso_Responsable
        fields = '__all__'

    def create(self, validated_data):
        recursoResponsable = super(RecursoResponsableSerializer,self).create(validated_data)
        recursoResponsable.save()
        return recursoResponsable

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.rescursos = validated_data.get('recursos', instance.rescursos)
        instance.responsable = validated_data.get('responsable', instance.responsable)
        instance.save()
        return instance

class TipoRecursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ['id']
        model = Tipo_Recurso
        fields = ('id','nombre')

class RecursoCreate(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields =('nombre','descripcion','tipo_Recurso','idSolicitud','idProyecto','descripcionSolicitud','estado')

    def create(self, validated_data):
        recurso = super(RecursoSerializer,self).create(validated_data)
        recurso.save()
        return recurso
class RecursoComentarioSerializer(serializers.ModelSerializer):
    nombre_responsable = serializers.CharField(source='revisor.nombres', read_only=True)
    apellidos_responsable = serializers.CharField(source='revisor.apellidos', read_only=True)
    usuario = serializers.CharField(source='revisor.usuario', read_only=True)
    class Meta:
        model = Control_Comentarios
        fields = '__all__'
