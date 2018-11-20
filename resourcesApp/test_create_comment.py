from unittest import TestCase
from resourcesApp.models import Control_Comentarios

import datetime

class TestCreateCommentario(TestCase):

    def setUp(self):
        Control_Comentarios.objects.create(idRecurso=1, comentario="Test Comentario 1", revisor="1",
                                           descripcion="Desc Prueba", fecha=datetime.datetime.now(), estado="creado")

    def test_comentario(self):
        tester = Control_Comentarios.objects.get(idRecurso="1")
        self.assertEqual(tester.comentario, 'Test Comentario 1')

