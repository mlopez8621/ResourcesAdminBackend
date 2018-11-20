from resourcesApp.models import Recurso


def setUp(self):
    Recurso.objects.create(idRecurso=10, nombre="Test Comentario 1", descripcion="descripcion recurso",
                           tipoRecurso=1, idSolicitud=1, idProyecto=1,descripcionSolicitud="solicitud prueba",
                           estado=1,auditor=1)


def test_get_auditor(self):
    auditor = Recurso.objects.get(pk=10)
    self.assertEqual(auditor.id, '10')