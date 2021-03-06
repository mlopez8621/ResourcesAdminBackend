from rest_framework import  serializers


from resourcesApp.models import Estado, Responsable, Recurso_Responsable, \
    Tipo_Recurso, Recurso, Control_Comentarios, Resultado_ListaChequeo,Recurso_Intermedio


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nombre','descripcion')

class RecursoSerializer(serializers.ModelSerializer):
    nombre_estado = serializers.CharField(source='estado.nombre', read_only=True)
    nombre_tipo = serializers.CharField(source='tipoRecurso.nombre', read_only=True)

    class Meta:
        model = Recurso
        fields = ('id', 'nombre','descripcion','tipoRecurso','idSolicitud','idProyecto','descripcionSolicitud','estado', 'nombre_estado', 'nombre_tipo','auditor')

    def create(self, validated_data):
        recurso = super(RecursoSerializer,self).create(validated_data)
        recurso.save()
        return recurso

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.auditor = validated_data.get('auditor', instance.auditor)
        print(instance)
        instance.save()
        return instance
class ResponsableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsable
        fields = '__all__'

class RecursoResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso_Responsable
        fields = '__all__'

class ResponsablePorRecursoSerializer(serializers.ModelSerializer):
    responsable =  ResponsableSerializer(read_only=True,allow_null=True)
    class Meta:
        model = Recurso_Responsable
        fields = '__all__'

class RecursoResponsableMostarSerializer(serializers.ModelSerializer):
    responsable = serializers.CharField(source='responsable.id', read_only=True)
    responsableName = serializers.CharField(source='responsable.nombres', read_only=True)
    #
    rescursos = serializers.CharField(source='rescursos.id', read_only=True)
    rescursosName = serializers.CharField(source='rescursos.nombre', read_only=True)

    class Meta:
        model = Recurso_Responsable
        # fields = ('id','responsable','responsableName','rescursos','rescursosName')
        fields = '__all__'


    def create(self, validated_data):
        recursoResponsable = super(RecursoResponsableSerializer,self).create(validated_data)
        recursoResponsable.save()
        return recursoResponsable

    def update(self, instance, validated_data):
        print(instance)
        instance.id = validated_data.get('id',instance.id)
        instance.rescursos = validated_data.get('recursos', instance.rescursos)
        instance.responsable = validated_data.get('responsable', instance.responsable)
        print(instance)
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

        
class ResultListCheqSerializer(serializers.ModelSerializer):
    nombre_recurso = serializers.CharField(source='recurso.nombre', read_only=True)
    nombre_item = serializers.CharField(source='itemChequeo.nombre', read_only=True)

    class Meta:
        model = Resultado_ListaChequeo
        fields = (
        'id', 'nombre_recurso', 'nombre_item', 'resultado')

class RecursosAuditorSerializer(serializers.ModelSerializer):
    auditor = ResponsableSerializer(read_only=True,allow_null=True)
    tipoRecurso=TipoRecursoSerializer(read_only=True,allow_null=True)
    class Meta:
        model = Recurso
        fields = '__all__'

class RecursoIntermedioSerializer(serializers.ModelSerializer):
    nombre_tipo_recurso = serializers.CharField(source='tipoRecurso.nombre', read_only=True)
    nombre_responsable = serializers.CharField(source='responsable.nombres', read_only=True)
    nombre_estado = serializers.CharField(source='estado.nombre', read_only=True)
    nombre_recursoPrincipal =serializers.CharField(source='recursoPrincipal.nombre', read_only=True)

    class Meta:
        model = Recurso_Intermedio
        fields = (
        'id',
        'nombre',
        'descripcion',
        'tipoRecurso',
        'nombre_tipo_recurso',
        'estado',
        'nombre_estado',
        'responsable',
        'nombre_responsable',
        'recursoPrincipal',
        'nombre_recursoPrincipal')