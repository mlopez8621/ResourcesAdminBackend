# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from resourcesApp.models import Recurso


def test_recurso_sin_comentarios(self):
    tester = Recurso.object.get(nombre="prueba_uno");
    print("*** " + tester);
    self.assertEqual(len(tester.comentarios), 0)