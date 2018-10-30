from unittest import TestCase

from resourcesApp.models import Recurso


class TestComentario(TestCase):

    def test_recurso_sin_comentarios(self):
        tester = Recurso.object.get(nombre="prueba_uno");
        print("*** "+tester);
        self.assertEqual(len(tester.comentarios), 0)


    def test_recurso_un_comentarios(self):
        tester = Recurso.object.get(nombre="prueba_dos");
        self.assertEqual(len(tester.comentarios), 1)
        self.assertEqual( not tester.comentarios[0], False)

    def test_varios_comentarios(self):
        tester = Recurso.object.get(nombre="prueba_tres");
        self.assertEqual(len(tester.comentarios), 3)
        self.assertEqual(not tester.comentarios[0], False)
        self.assertEqual(not tester.comentarios[1], False)
        self.assertEqual(not tester.comentarios[2], False)


