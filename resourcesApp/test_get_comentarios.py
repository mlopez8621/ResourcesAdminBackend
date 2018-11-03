from unittest import TestCase

from resourcesApp.Views.RecursoViews import recursos_comentarios


class TestComentario(TestCase):

    def test_recurso_sin_comentarios(self):
        tester = recursos_comentarios;
        self.assertEqual(len(tester.comentario), 0)


    def test_recurso_un_comentarios(self):
        tester = recursos_comentarios(1);
        self.assertEqual(len(tester.comentario), 1)
        self.assertEqual( not tester.comentario[0], False)

    def test_varios_comentarios(self):
        tester = recursos_comentarios(2);
        self.assertEqual(len(tester.comentario), 3)
        self.assertEqual(not tester.comentario[0], False)
        self.assertEqual(not tester.comentario[1], False)
        self.assertEqual(not tester.comentario[2], False)


